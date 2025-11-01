"""
AstraTerm API - FastAPI Backend
Provides REST API and WebSocket endpoints for terminal functionality
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict
import asyncio
import subprocess
import json
import uuid
from datetime import datetime

# Import AstraTerm modules
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from astraterm.ai_assistant import AIAssistant
from astraterm.config import load_config

app = FastAPI(
    title="AstraTerm API",
    description="AI-Powered Terminal API",
    version="1.2.0"
)

# CORS configuration for web frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load configuration
config = load_config()
ai_assistant = AIAssistant(config)

# Session management
sessions: Dict[str, dict] = {}


# Pydantic Models
class CommandRequest(BaseModel):
    command: str
    session_id: Optional[str] = None


class AIRequest(BaseModel):
    prompt: str
    provider: Optional[str] = "grok"


class GitHubSearchRequest(BaseModel):
    query: str


class SessionResponse(BaseModel):
    session_id: str
    created_at: str


class CommandResponse(BaseModel):
    output: str
    error: Optional[str] = None
    exit_code: Optional[int] = None


class AIResponse(BaseModel):
    response: str
    provider: str


# Helper functions
def create_session() -> str:
    """Create a new terminal session"""
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "created_at": datetime.now().isoformat(),
        "history": [],
        "cwd": str(Path.home())
    }
    return session_id


def execute_command(command: str, cwd: str = None) -> Dict:
    """Execute a shell command safely"""
    try:
        # Security: Restrict dangerous commands
        dangerous_commands = ["rm -rf /", "mkfs", "dd if=", "> /dev/"]
        if any(dangerous in command for dangerous in dangerous_commands):
            return {
                "output": "",
                "error": "Command not allowed for security reasons",
                "exit_code": 1
            }
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=cwd
        )
        
        return {
            "output": result.stdout,
            "error": result.stderr if result.returncode != 0 else None,
            "exit_code": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {
            "output": "",
            "error": "Command timeout (30s limit)",
            "exit_code": 124
        }
    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "exit_code": 1
        }


# API Endpoints
@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "name": "AstraTerm API",
        "version": "1.2.0",
        "status": "running",
        "endpoints": {
            "sessions": "/api/sessions",
            "command": "/api/command",
            "ai": "/api/ai",
            "github": "/api/github",
            "websocket": "/ws/{session_id}"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/api/sessions", response_model=SessionResponse)
async def create_new_session():
    """Create a new terminal session"""
    session_id = create_session()
    return SessionResponse(
        session_id=session_id,
        created_at=sessions[session_id]["created_at"]
    )


@app.get("/api/sessions/{session_id}")
async def get_session(session_id: str):
    """Get session information"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return sessions[session_id]


@app.delete("/api/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a terminal session"""
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions[session_id]
    return {"message": "Session deleted"}


@app.post("/api/command", response_model=CommandResponse)
async def execute_terminal_command(request: CommandRequest):
    """Execute a terminal command"""
    session_id = request.session_id
    
    # Create session if not provided
    if not session_id or session_id not in sessions:
        session_id = create_session()
    
    session = sessions[session_id]
    
    # Handle special commands
    if request.command == "clear":
        return CommandResponse(output="", error=None, exit_code=0)
    
    if request.command.startswith("cd "):
        # Handle directory change
        new_dir = request.command[3:].strip()
        try:
            target_path = Path(session["cwd"]) / new_dir
            if target_path.exists() and target_path.is_dir():
                session["cwd"] = str(target_path.resolve())
                return CommandResponse(output="", error=None, exit_code=0)
            else:
                return CommandResponse(
                    output="",
                    error=f"Directory not found: {new_dir}",
                    exit_code=1
                )
        except Exception as e:
            return CommandResponse(output="", error=str(e), exit_code=1)
    
    # Execute command
    result = execute_command(request.command, session["cwd"])
    
    # Store in history
    session["history"].append({
        "command": request.command,
        "timestamp": datetime.now().isoformat(),
        "output": result["output"],
        "error": result["error"]
    })
    
    return CommandResponse(**result)


@app.post("/api/ai", response_model=AIResponse)
async def ai_query(request: AIRequest):
    """Get AI assistance"""
    try:
        response = ai_assistant.get_code_hint(request.prompt, request.provider)
        return AIResponse(response=response, provider=request.provider)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/github")
async def github_search(request: GitHubSearchRequest):
    """Search GitHub repositories"""
    try:
        results = ai_assistant.github_search(request.query)
        return {"results": results[:10]}  # Limit to 10 results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/config")
async def get_config():
    """Get public configuration (without API keys)"""
    return {
        "has_xai_key": bool(config.get("xai_api_key")),
        "has_openai_key": bool(config.get("openai_api_key")),
        "has_anthropic_key": bool(config.get("anthropic_api_key")),
        "has_deepseek_key": bool(config.get("deepseek_api_key")),
        "has_github_token": bool(config.get("github_token"))
    }


# WebSocket endpoint for real-time terminal
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    """WebSocket endpoint for real-time terminal interaction"""
    await websocket.accept()
    
    # Create session if it doesn't exist
    if session_id not in sessions:
        sessions[session_id] = {
            "created_at": datetime.now().isoformat(),
            "history": [],
            "cwd": str(Path.home())
        }
    
    try:
        # Send welcome message
        await websocket.send_json({
            "type": "welcome",
            "message": "Connected to AstraTerm API v1.2.0",
            "session_id": session_id
        })
        
        while True:
            # Receive command from client
            data = await websocket.receive_json()
            command = data.get("command", "")
            
            if not command:
                continue
            
            # Handle special commands
            if command == "exit" or command == "quit":
                await websocket.send_json({
                    "type": "exit",
                    "message": "Goodbye!"
                })
                break
            
            # Execute command
            session = sessions[session_id]
            result = execute_command(command, session["cwd"])
            
            # Send response
            await websocket.send_json({
                "type": "output",
                "command": command,
                "output": result["output"],
                "error": result["error"],
                "exit_code": result["exit_code"]
            })
            
    except WebSocketDisconnect:
        print(f"WebSocket disconnected: {session_id}")
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        await websocket.send_json({
            "type": "error",
            "message": str(e)
        })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
