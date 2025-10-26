# astraterm/main.py
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input
from textual.containers import Grid
from .terminal import TerminalSession
from .ai_assistant import AIAssistant
from .config import load_config

class AstraTermApp(App):
    CSS = """
    Screen {
        background: #1e1e1e;
    }
    Header {
        background: #007acc;
    }
    Footer {
        background: #007acc;
    }
    """
    BINDINGS = [
        ("ctrl+w", "split_window", "Split Window"),
        ("ctrl+g", "open_github_popup", "GitHub Search"),
        ("ctrl+space", "toggle_ai", "AI Assistant"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Grid(TerminalSession(), id="main-grid")
        yield Input(placeholder="Search or type command...")
        yield Footer()

    def on_mount(self):
        self.config = load_config()
        self.ai = AIAssistant(self.config)
        self.terminal = TerminalSession()

    def action_split_window(self):
        self.query_one("#main-grid").add_child(TerminalSession())

    def action_open_github_popup(self):
        self.push_screen(GitHubSearchPopup())  # From github.py

    def action_toggle_ai(self):
        # Toggle AI overlay (implement as needed)
        pass

if __name__ == "__main__":
    AstraTermApp().run()
