# astraterm/github.py
from textual.screen import ModalScreen
from textual.widgets import ListView, ListItem

class GitHubSearchPopup(ModalScreen):
    def __init__(self, results: list):
        super().__init__()
        self.results = results

    def compose(self):
        yield ListView(*[ListItem(repo["full_name"]) for repo in self.results])
