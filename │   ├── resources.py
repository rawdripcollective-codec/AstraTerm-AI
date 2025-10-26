# astraterm/resources.py
import requests

class ResourceUpdater:
    def fetch_cheat_sheet(self, lang: str):
        # Simulate fetch
        return f"Cheat sheet for {lang}: print('Hello World')"

    def install_lib(self, lib: str):
        # Use pip in subprocess (for demo)
        subprocess.run(["pip", "install", lib])
