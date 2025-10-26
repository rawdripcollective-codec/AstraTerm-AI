# tests/test_terminal.py
import pytest
from astraterm.terminal import TerminalSession

def test_run_command():
    session = TerminalSession()
    assert "Hello" in session.run_command("echo Hello")
