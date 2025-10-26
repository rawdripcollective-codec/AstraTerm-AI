# astraterm/plugins.py
from importlib import import_module

class PluginManager:
    def load(self, name: str):
        try:
            return import_module(f"astraterm.plugins.{name}")
        except ImportError:
            return None
