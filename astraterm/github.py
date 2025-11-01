# astraterm/github.py
from textual.screen import ModalScreen
from textual.widgets import ListView, ListItem, Label
from textual.containers import Container
from typing import List, Dict

class GitHubSearchPopup(ModalScreen):
    """Modal screen for displaying GitHub search results"""
    
    def __init__(self, results: List[Dict]):
        super().__init__()
        self.results = results

    def compose(self):
        """Compose the UI for GitHub search results"""
        if not self.results:
            yield Container(
                Label("No results found"),
                id="github-popup"
            )
        else:
            items = []
            for repo in self.results:
                name = repo.get("full_name", "Unknown")
                description = repo.get("description", "No description")
                stars = repo.get("stargazers_count", 0)
                label = f"{name} ⭐ {stars}\n{description}"
                items.append(ListItem(Label(label)))
            
            yield Container(
                Label("GitHub Search Results", id="popup-title"),
                ListView(*items),
                id="github-popup"
            )

    def on_list_view_selected(self, event):
        """Handle repository selection"""
        if self.results:
            selected_index = event.list_view.index
            if 0 <= selected_index < len(self.results):
                repo = self.results[selected_index]
                # Open repository URL or perform action
                self.dismiss(repo)
