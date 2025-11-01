# astraterm/osint.py
import subprocess
import shutil
from typing import Optional, List, Dict

class OSINTTools:
    """OSINT (Open Source Intelligence) Tools Integration"""
    
    TOOLS = [
        "maltego",
        "shodan",
        "recon-ng",
        "spiderfoot",
        "theharvester",
        "sherlock",
        "haveibeenpwned",
        "intelligencex",
        "pimeyes",
        "eyeofgod"
    ]
    
    def __init__(self):
        self.available_tools = self._check_available_tools()

    def _check_available_tools(self) -> List[str]:
        """Check which OSINT tools are installed"""
        available = []
        for tool in self.TOOLS:
            if shutil.which(tool):
                available.append(tool)
        return available

    def is_tool_available(self, tool: str) -> bool:
        """Check if a specific tool is available"""
        return tool in self.available_tools

    def run_tool(self, tool: str, target: str, args: str = "") -> str:
        """
        Run an OSINT tool on a target
        
        Args:
            tool: Name of the OSINT tool
            target: Target to investigate
            args: Additional arguments for the tool
        
        Returns:
            Tool output or error message
        """
        if tool not in self.TOOLS:
            return f"Unknown tool: {tool}. Available: {', '.join(self.TOOLS)}"
        
        if tool == "eyeofgod":
            return self._run_eyeofgod(target)
        elif tool == "sherlock":
            return self._run_sherlock(target, args)
        elif tool == "theharvester":
            return self._run_theharvester(target, args)
        elif tool == "shodan":
            return self._run_shodan(target, args)
        elif tool == "haveibeenpwned":
            return self._run_haveibeenpwned(target)
        else:
            return f"Tool {tool} integration not yet implemented"

    def _run_eyeofgod(self, target: str) -> str:
        """Run Eye of God search (Telegram-based OSINT)"""
        # Eye of God is a Telegram bot, this is a placeholder
        return f"Eye of God search for '{target}':\n" \
               f"Note: Eye of God requires Telegram bot integration.\n" \
               f"Please use the Telegram bot directly: @EyeofGodBot"

    def _run_sherlock(self, username: str, args: str = "") -> str:
        """Run Sherlock to find social media accounts"""
        if not shutil.which("sherlock"):
            return "Sherlock is not installed. Install with: pip install sherlock-project"
        
        try:
            cmd = ["sherlock", username]
            if args:
                cmd.extend(args.split())
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout or result.stderr
        except subprocess.TimeoutExpired:
            return "Sherlock search timed out"
        except Exception as e:
            return f"Error running Sherlock: {str(e)}"

    def _run_theharvester(self, domain: str, args: str = "-b all") -> str:
        """Run theHarvester for email and subdomain enumeration"""
        if not shutil.which("theharvester"):
            return "theHarvester is not installed. Install with: pip install theharvester"
        
        try:
            cmd = ["theharvester", "-d", domain]
            if args:
                cmd.extend(args.split())
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            return result.stdout or result.stderr
        except subprocess.TimeoutExpired:
            return "theHarvester search timed out"
        except Exception as e:
            return f"Error running theHarvester: {str(e)}"

    def _run_shodan(self, query: str, args: str = "") -> str:
        """Run Shodan search"""
        if not shutil.which("shodan"):
            return "Shodan CLI is not installed. Install with: pip install shodan"
        
        try:
            cmd = ["shodan", "search", query]
            if args:
                cmd.extend(args.split())
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout or result.stderr
        except subprocess.TimeoutExpired:
            return "Shodan search timed out"
        except Exception as e:
            return f"Error running Shodan: {str(e)}"

    def _run_haveibeenpwned(self, email: str) -> str:
        """Check if email has been in a data breach"""
        try:
            import requests
            
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {
                "User-Agent": "AstraTerm-OSINT"
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                breaches = response.json()
                result = f"Email '{email}' found in {len(breaches)} breaches:\n"
                for breach in breaches:
                    result += f"  - {breach['Name']} ({breach['BreachDate']})\n"
                return result
            elif response.status_code == 404:
                return f"Good news! Email '{email}' not found in any breaches."
            else:
                return f"Error checking email: HTTP {response.status_code}"
        except Exception as e:
            return f"Error checking Have I Been Pwned: {str(e)}"

    def list_tools(self) -> str:
        """List all available OSINT tools"""
        result = "OSINT Tools:\n"
        for tool in self.TOOLS:
            status = "✓ Installed" if tool in self.available_tools else "✗ Not installed"
            result += f"  {tool}: {status}\n"
        return result
