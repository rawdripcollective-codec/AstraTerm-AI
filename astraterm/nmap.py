# astraterm/nmap.py
import subprocess
import shutil
from typing import Optional, Dict, List

class NmapScanner:
    """Network scanning using Nmap"""
    
    def __init__(self):
        self.installed = self.is_installed()
        self.last_scan = None

    def is_installed(self) -> bool:
        """Check if nmap is installed"""
        return shutil.which("nmap") is not None

    def install(self) -> bool:
        """Install nmap"""
        try:
            result = subprocess.run(
                ["apt", "install", "-y", "nmap"],
                capture_output=True,
                text=True,
                timeout=120
            )
            self.installed = result.returncode == 0
            return self.installed
        except Exception as e:
            print(f"Error installing nmap: {str(e)}")
            return False

    def scan(self, target: str, args: str = "-sV -sC") -> Optional[str]:
        """
        Scan a target with nmap
        
        Args:
            target: IP address or hostname to scan
            args: Nmap arguments (default: -sV -sC for version detection and default scripts)
        
        Returns:
            Scan output as string or None on error
        """
        if not self.installed:
            return "Nmap is not installed. Run install() first."
        
        try:
            cmd = ["nmap"] + args.split() + [target]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            self.last_scan = result.stdout
            return result.stdout
        except subprocess.TimeoutExpired:
            return "Scan timed out"
        except Exception as e:
            return f"Error: {str(e)}"

    def quick_scan(self, target: str) -> Optional[str]:
        """Quick scan of most common ports"""
        return self.scan(target, "-F")

    def stealth_scan(self, target: str) -> Optional[str]:
        """Stealth SYN scan"""
        return self.scan(target, "-sS")

    def udp_scan(self, target: str) -> Optional[str]:
        """UDP port scan"""
        return self.scan(target, "-sU")

    def os_detection(self, target: str) -> Optional[str]:
        """OS detection scan"""
        return self.scan(target, "-O")

    def aggressive_scan(self, target: str) -> Optional[str]:
        """Aggressive scan with OS detection, version detection, script scanning, and traceroute"""
        return self.scan(target, "-A")

    def ping_sweep(self, network: str) -> Optional[str]:
        """Ping sweep of a network"""
        return self.scan(network, "-sn")

    def save_scan(self, filename: str) -> bool:
        """Save last scan results to file"""
        if not self.last_scan:
            print("No scan results to save")
            return False
        
        try:
            with open(filename, "w") as f:
                f.write(self.last_scan)
            return True
        except Exception as e:
            print(f"Error saving scan: {str(e)}")
            return False
