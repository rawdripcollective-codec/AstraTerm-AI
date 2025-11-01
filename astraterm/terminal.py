# astraterm/terminal.py
import subprocess
from textual.widgets import Static, RichLog
from textual.reactive import reactive
from rich.text import Text
from pathlib import Path
from typing import List, Tuple, Optional

class TerminalSession(RichLog):
    """Terminal session widget with command execution and history"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history: List[Tuple[str, str]] = []
        self.current_dir = Path.cwd()
        self.max_lines = 1000

    def run_command(self, cmd: str) -> str:
        """
        Execute a shell command and return output
        
        Args:
            cmd: Command to execute
        
        Returns:
            Command output (stdout or stderr)
        """
        if not cmd.strip():
            return ""
        
        # Handle cd command specially
        if cmd.strip().startswith("cd "):
            return self._handle_cd(cmd.strip()[3:].strip())
        
        # Handle clear command
        if cmd.strip() == "clear":
            self.clear()
            return ""
        
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                cwd=str(self.current_dir),
                timeout=30
            )
            
            output = result.stdout if result.stdout else result.stderr
            self.history.append((cmd, output))
            
            # Write to log
            self.write(Text(f"$ {cmd}", style="bold cyan"))
            if output:
                self.write(output)
            
            return output
        except subprocess.TimeoutExpired:
            error = "Command timed out (30s limit)"
            self.history.append((cmd, error))
            self.write(Text(error, style="bold red"))
            return error
        except Exception as e:
            error = f"Error: {str(e)}"
            self.history.append((cmd, error))
            self.write(Text(error, style="bold red"))
            return error

    def _handle_cd(self, path: str) -> str:
        """Handle directory change"""
        try:
            if not path or path == "~":
                new_dir = Path.home()
            else:
                new_dir = (self.current_dir / path).resolve()
            
            if new_dir.exists() and new_dir.is_dir():
                self.current_dir = new_dir
                return f"Changed directory to: {self.current_dir}"
            else:
                return f"Directory not found: {path}"
        except Exception as e:
            return f"Error changing directory: {str(e)}"

    def get_prompt(self) -> str:
        """Get current prompt string"""
        return f"{self.current_dir.name}$ "

    def save_session(self, filename: str) -> bool:
        """
        Save command history to file
        
        Args:
            filename: Output file path
        
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, "w") as f:
                f.write("# AstraTerm Session History\n")
                f.write(f"# Working Directory: {self.current_dir}\n\n")
                for cmd, output in self.history:
                    f.write(f"$ {cmd}\n")
                    if output:
                        f.write(f"{output}\n")
                    f.write("\n")
            return True
        except Exception as e:
            self.write(Text(f"Error saving session: {str(e)}", style="bold red"))
            return False

    def load_session(self, filename: str) -> bool:
        """
        Load and replay commands from a session file
        
        Args:
            filename: Input file path
        
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                if line.startswith("$ "):
                    cmd = line[2:]
                    self.run_command(cmd)
            
            return True
        except Exception as e:
            self.write(Text(f"Error loading session: {str(e)}", style="bold red"))
            return False

    def clear_history(self):
        """Clear command history"""
        self.history.clear()

    def get_history(self) -> List[str]:
        """Get list of executed commands"""
        return [cmd for cmd, _ in self.history]

    def search_history(self, query: str) -> List[Tuple[str, str]]:
        """Search command history"""
        return [(cmd, output) for cmd, output in self.history if query.lower() in cmd.lower()]
