# astraterm/config.py
import json
import os
from pathlib import Path

def load_config(file="config.json"):
    """Load configuration from JSON file"""
    config_path = Path(file)
    
    # Try to load from current directory first
    if not config_path.exists():
        # Try home directory
        config_path = Path.home() / ".astraterm" / "config.json"
    
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Return default configuration
        return {
            "xai_api_key": "",
            "github_token": "",
            "openai_api_key": "",
            "anthropic_api_key": "",
            "deepseek_api_key": ""
        }

def save_config(config, file="config.json"):
    """Save configuration to JSON file"""
    config_path = Path(file)
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
