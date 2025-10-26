# astraterm/config.py
import json

def load_config(file="config.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Default keys: xai_api_key, etc.
