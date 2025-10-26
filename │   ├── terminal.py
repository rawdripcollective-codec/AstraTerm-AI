# astraterm/terminal.py
import subprocess
from textual.widgets import Static

class TerminalSession(Static):
    def __init__(self):
        super().__init__()
        self.history = []

    def run_command(self, cmd: str) -> str:
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            self.history.append((cmd, result.stdout or result.stderr))
            return result.stdout or result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    def save_session(self, filename: str):
        with open(filename, "w") as f:
            f.write("\n".join(cmd for cmd, _ in self.history))
