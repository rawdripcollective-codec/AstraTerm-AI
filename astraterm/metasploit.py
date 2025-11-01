# astraterm/metasploit.py
import subprocess
import shutil
from typing import Optional

class Metasploit:
    """Metasploit Framework integration"""
    
    def __init__(self):
        self.installed = self.is_installed()

    def is_installed(self) -> bool:
        """Check if Metasploit is installed"""
        return shutil.which("msfconsole") is not None

    def install(self) -> bool:
        """Install Metasploit Framework"""
        try:
            # Check if running on Debian/Ubuntu-based system
            result = subprocess.run(
                ["apt", "install", "-y", "metasploit-framework"],
                capture_output=True,
                text=True,
                timeout=600
            )
            self.installed = result.returncode == 0
            return self.installed
        except subprocess.TimeoutExpired:
            print("Metasploit installation timed out")
            return False
        except Exception as e:
            print(f"Error installing Metasploit: {str(e)}")
            return False

    def run_console(self) -> bool:
        """Run Metasploit console"""
        if not self.installed:
            print("Metasploit is not installed. Run install() first.")
            return False
        
        try:
            subprocess.run(["msfconsole"])
            return True
        except Exception as e:
            print(f"Error running msfconsole: {str(e)}")
            return False

    def run_command(self, command: str) -> Optional[str]:
        """Run a Metasploit command and return output"""
        if not self.installed:
            return "Metasploit is not installed"
        
        try:
            result = subprocess.run(
                ["msfconsole", "-q", "-x", f"{command}; exit"],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            return "Command timed out"
        except Exception as e:
            return f"Error: {str(e)}"

    def update(self) -> bool:
        """Update Metasploit Framework"""
        if not self.installed:
            print("Metasploit is not installed")
            return False
        
        try:
            result = subprocess.run(
                ["msfupdate"],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Error updating Metasploit: {str(e)}")
            return False
