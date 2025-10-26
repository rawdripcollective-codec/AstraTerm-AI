# astraterm/ai_assistant.py
import requests
from xai_sdk import Client  # Assuming installed
# Import OpenAI, Anthropic as needed

class AIAssistant:
    def __init__(self, config):
        self.grok = Client(api_key=config.get("xai_api_key"))
        # Add OpenAI, Claude, Deepseek similarly

    def get_code_hint(self, code: str) -> str:
        response = self.grok.chat.completions.create(
            model="grok-4",
            messages=[{"role": "user", "content": f"Complete: {code}"}]
        )
        return response.choices[0].message.content

    def github_search(self, query: str) -> list:
        headers = {"Authorization": f"Bearer {self.config.get('github_token')}"}
        resp = requests.get(f"https://api.github.com/search/repositories?q={query}", headers=headers)
        return resp.json().get("items", []) if resp.ok else []
