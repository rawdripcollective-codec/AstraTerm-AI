# astraterm/ai_assistant.py
import requests
from typing import Optional, Dict, List

class AIAssistant:
    """AI Assistant supporting multiple AI providers"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.xai_api_key = config.get("xai_api_key", "")
        self.openai_api_key = config.get("openai_api_key", "")
        self.anthropic_api_key = config.get("anthropic_api_key", "")
        self.deepseek_api_key = config.get("deepseek_api_key", "")
        self.github_token = config.get("github_token", "")

    def get_code_hint(self, code: str, provider: str = "grok") -> str:
        """Get code completion hint from AI provider"""
        try:
            if provider == "grok" and self.xai_api_key:
                return self._grok_completion(code)
            elif provider == "openai" and self.openai_api_key:
                return self._openai_completion(code)
            elif provider == "claude" and self.anthropic_api_key:
                return self._claude_completion(code)
            elif provider == "deepseek" and self.deepseek_api_key:
                return self._deepseek_completion(code)
            else:
                return "No API key configured for selected provider"
        except Exception as e:
            return f"Error: {str(e)}"

    def _grok_completion(self, code: str) -> str:
        """Get completion from Grok (xAI)"""
        try:
            # Using xAI API
            headers = {
                "Authorization": f"Bearer {self.xai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "grok-beta",
                "messages": [
                    {"role": "system", "content": "You are a helpful coding assistant."},
                    {"role": "user", "content": f"Complete this code:\n{code}"}
                ]
            }
            response = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            if response.ok:
                return response.json()["choices"][0]["message"]["content"]
            return f"Error: {response.status_code}"
        except Exception as e:
            return f"Grok API Error: {str(e)}"

    def _openai_completion(self, code: str) -> str:
        """Get completion from OpenAI"""
        try:
            headers = {
                "Authorization": f"Bearer {self.openai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "gpt-4",
                "messages": [
                    {"role": "system", "content": "You are a helpful coding assistant."},
                    {"role": "user", "content": f"Complete this code:\n{code}"}
                ]
            }
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            if response.ok:
                return response.json()["choices"][0]["message"]["content"]
            return f"Error: {response.status_code}"
        except Exception as e:
            return f"OpenAI API Error: {str(e)}"

    def _claude_completion(self, code: str) -> str:
        """Get completion from Claude (Anthropic)"""
        try:
            headers = {
                "x-api-key": self.anthropic_api_key,
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01"
            }
            data = {
                "model": "claude-3-opus-20240229",
                "messages": [
                    {"role": "user", "content": f"Complete this code:\n{code}"}
                ],
                "max_tokens": 1024
            }
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=data,
                timeout=30
            )
            if response.ok:
                return response.json()["content"][0]["text"]
            return f"Error: {response.status_code}"
        except Exception as e:
            return f"Claude API Error: {str(e)}"

    def _deepseek_completion(self, code: str) -> str:
        """Get completion from DeepSeek"""
        try:
            headers = {
                "Authorization": f"Bearer {self.deepseek_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are a helpful coding assistant."},
                    {"role": "user", "content": f"Complete this code:\n{code}"}
                ]
            }
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            if response.ok:
                return response.json()["choices"][0]["message"]["content"]
            return f"Error: {response.status_code}"
        except Exception as e:
            return f"DeepSeek API Error: {str(e)}"

    def github_search(self, query: str) -> List[Dict]:
        """Search GitHub repositories"""
        try:
            headers = {}
            if self.github_token:
                headers["Authorization"] = f"Bearer {self.github_token}"
            
            response = requests.get(
                f"https://api.github.com/search/repositories?q={query}",
                headers=headers,
                timeout=10
            )
            
            if response.ok:
                return response.json().get("items", [])
            return []
        except Exception as e:
            print(f"GitHub search error: {str(e)}")
            return []
