# astraterm/main.py
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Label
from textual.containers import Container, Vertical
from textual.binding import Binding
from .terminal import TerminalSession
from .ai_assistant import AIAssistant
from .github import GitHubSearchPopup
from .config import load_config

class AstraTermApp(App):
    """AstraTerm - AI-Powered Terminal Application"""
    
    CSS = """
    Screen {
        background: #1e1e1e;
    }
    
    Header {
        background: #007acc;
        color: white;
    }
    
    Footer {
        background: #007acc;
        color: white;
    }
    
    #main-container {
        height: 100%;
        padding: 1;
    }
    
    #terminal-container {
        height: 1fr;
        border: solid #007acc;
        margin: 1;
    }
    
    #input-container {
        height: auto;
        padding: 1;
    }
    
    Input {
        width: 100%;
    }
    
    .status-bar {
        background: #2d2d2d;
        color: #cccccc;
        padding: 0 1;
    }
    """
    
    BINDINGS = [
        Binding("ctrl+w", "split_window", "Split Window", show=True),
        Binding("ctrl+g", "open_github_popup", "GitHub Search", show=True),
        Binding("ctrl+space", "toggle_ai", "AI Assistant", show=True),
        Binding("ctrl+q", "quit", "Quit", show=True),
        Binding("ctrl+l", "clear_terminal", "Clear", show=True),
    ]
    
    TITLE = "AstraTerm AI v1.2.0"

    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.ai = AIAssistant(self.config)
        self.terminal = None

    def compose(self) -> ComposeResult:
        """Compose the UI"""
        yield Header(show_clock=True)
        
        with Container(id="main-container"):
            with Vertical(id="terminal-container"):
                self.terminal = TerminalSession()
                yield self.terminal
            
            with Container(id="input-container"):
                yield Label("Command:", classes="status-bar")
                yield Input(placeholder="Enter command or type 'help' for assistance...", id="command-input")
        
        yield Footer()

    def on_mount(self):
        """Called when app is mounted"""
        self.terminal.write("Welcome to AstraTerm AI v1.2.0")
        self.terminal.write("Type 'help' for available commands")
        self.terminal.write("")
        
        # Focus on input
        self.query_one("#command-input").focus()

    def on_input_submitted(self, event: Input.Submitted):
        """Handle command input"""
        command = event.value.strip()
        
        if not command:
            return
        
        # Clear input
        event.input.value = ""
        
        # Handle special commands
        if command == "help":
            self._show_help()
        elif command == "exit" or command == "quit":
            self.exit()
        elif command.startswith("ai "):
            self._handle_ai_command(command[3:])
        elif command.startswith("github "):
            self._handle_github_search(command[7:])
        else:
            # Execute as shell command
            self.terminal.run_command(command)

    def _show_help(self):
        """Show help information"""
        help_text = """
AstraTerm AI Commands:
  help              - Show this help message
  clear             - Clear terminal
  exit/quit         - Exit application
  ai <prompt>       - Get AI assistance
  github <query>    - Search GitHub repositories
  
Keyboard Shortcuts:
  Ctrl+W            - Split window
  Ctrl+G            - GitHub search popup
  Ctrl+Space        - Toggle AI assistant
  Ctrl+L            - Clear terminal
  Ctrl+Q            - Quit application
  
Shell Commands:
  Any other command will be executed as a shell command
"""
        self.terminal.write(help_text)

    def _handle_ai_command(self, prompt: str):
        """Handle AI assistant command"""
        self.terminal.write(f"AI Query: {prompt}")
        response = self.ai.get_code_hint(prompt)
        self.terminal.write(f"AI Response:\n{response}")

    def _handle_github_search(self, query: str):
        """Handle GitHub search command"""
        self.terminal.write(f"Searching GitHub for: {query}")
        results = self.ai.github_search(query)
        
        if results:
            self.terminal.write(f"Found {len(results)} repositories:")
            for i, repo in enumerate(results[:5], 1):
                name = repo.get("full_name", "Unknown")
                stars = repo.get("stargazers_count", 0)
                desc = repo.get("description", "No description")
                self.terminal.write(f"{i}. {name} (⭐ {stars})")
                self.terminal.write(f"   {desc}")
        else:
            self.terminal.write("No results found")

    def action_split_window(self):
        """Split terminal window"""
        self.terminal.write("Split window feature coming soon!")

    def action_open_github_popup(self):
        """Open GitHub search popup"""
        # For now, just show a message
        self.terminal.write("GitHub popup feature - use 'github <query>' command")

    def action_toggle_ai(self):
        """Toggle AI assistant overlay"""
        self.terminal.write("AI assistant overlay coming soon!")

    def action_clear_terminal(self):
        """Clear terminal"""
        self.terminal.clear()

def run_app():
    """Entry point for the application"""
    app = AstraTermApp()
    app.run()

if __name__ == "__main__":
    run_app()
