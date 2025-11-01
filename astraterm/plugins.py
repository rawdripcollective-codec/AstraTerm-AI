# astraterm/plugins.py
from importlib import import_module
from pathlib import Path
from typing import Optional, List, Dict
import sys

class PluginManager:
    """Manage AstraTerm plugins"""
    
    def __init__(self, plugin_dir: str = "plugins"):
        self.plugin_dir = Path(plugin_dir)
        self.loaded_plugins: Dict[str, object] = {}
        self._ensure_plugin_dir()

    def _ensure_plugin_dir(self):
        """Ensure plugin directory exists"""
        if not self.plugin_dir.exists():
            self.plugin_dir.mkdir(parents=True, exist_ok=True)
            # Create __init__.py for plugins package
            init_file = self.plugin_dir / "__init__.py"
            if not init_file.exists():
                init_file.write_text("# AstraTerm Plugins\n")

    def load(self, name: str) -> Optional[object]:
        """
        Load a plugin by name
        
        Args:
            name: Plugin name (without .py extension)
        
        Returns:
            Loaded plugin module or None if not found
        """
        if name in self.loaded_plugins:
            return self.loaded_plugins[name]
        
        try:
            # Try loading from astraterm.plugins package
            module = import_module(f"astraterm.plugins.{name}")
            self.loaded_plugins[name] = module
            return module
        except ImportError:
            try:
                # Try loading from custom plugins directory
                plugin_path = self.plugin_dir / f"{name}.py"
                if plugin_path.exists():
                    spec = import_module(f"{self.plugin_dir.name}.{name}")
                    self.loaded_plugins[name] = spec
                    return spec
            except ImportError:
                pass
        
        return None

    def unload(self, name: str) -> bool:
        """Unload a plugin"""
        if name in self.loaded_plugins:
            del self.loaded_plugins[name]
            return True
        return False

    def list_plugins(self) -> List[str]:
        """List all available plugins"""
        plugins = []
        
        # List plugins in plugin directory
        if self.plugin_dir.exists():
            for file in self.plugin_dir.glob("*.py"):
                if file.name != "__init__.py":
                    plugins.append(file.stem)
        
        return plugins

    def reload(self, name: str) -> Optional[object]:
        """Reload a plugin"""
        if name in self.loaded_plugins:
            self.unload(name)
        return self.load(name)

    def get_loaded_plugins(self) -> List[str]:
        """Get list of currently loaded plugins"""
        return list(self.loaded_plugins.keys())

    def execute_plugin(self, name: str, method: str, *args, **kwargs):
        """
        Execute a method from a loaded plugin
        
        Args:
            name: Plugin name
            method: Method name to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
        
        Returns:
            Method return value or None
        """
        plugin = self.loaded_plugins.get(name)
        if not plugin:
            plugin = self.load(name)
        
        if plugin and hasattr(plugin, method):
            func = getattr(plugin, method)
            if callable(func):
                return func(*args, **kwargs)
        
        return None
