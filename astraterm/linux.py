# astraterm/linux.py
import subprocess
import shutil
from typing import Optional

class LinuxDistro:
    """Manage Linux distributions using proot-distro"""
    
    SUPPORTED_DISTROS = [
        "alpine", "archlinux", "debian", "fedora", "kali",
        "ubuntu", "void", "manjaro", "parrot"
    ]
    
    def __init__(self, distro: str = "kali"):
        if distro not in self.SUPPORTED_DISTROS:
            raise ValueError(f"Unsupported distro: {distro}. Supported: {', '.join(self.SUPPORTED_DISTROS)}")
        self.distro = distro

    def is_proot_installed(self) -> bool:
        """Check if proot-distro is installed"""
        return shutil.which("proot-distro") is not None

    def install(self) -> bool:
        """Install the Linux distribution"""
        if not self.is_proot_installed():
            print("Error: proot-distro is not installed")
            return False
        
        try:
            result = subprocess.run(
                ["proot-distro", "install", self.distro],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            print(f"Installation of {self.distro} timed out")
            return False
        except Exception as e:
            print(f"Error installing {self.distro}: {str(e)}")
            return False

    def start(self) -> bool:
        """Start/login to the Linux distribution"""
        if not self.is_proot_installed():
            print("Error: proot-distro is not installed")
            return False
        
        try:
            subprocess.run(["proot-distro", "login", self.distro])
            return True
        except Exception as e:
            print(f"Error starting {self.distro}: {str(e)}")
            return False

    def list_installed(self) -> list:
        """List installed distributions"""
        if not self.is_proot_installed():
            return []
        
        try:
            result = subprocess.run(
                ["proot-distro", "list"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return result.stdout.strip().split("\n")
            return []
        except Exception:
            return []

    def remove(self) -> bool:
        """Remove the Linux distribution"""
        if not self.is_proot_installed():
            print("Error: proot-distro is not installed")
            return False
        
        try:
            result = subprocess.run(
                ["proot-distro", "remove", self.distro],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Error removing {self.distro}: {str(e)}")
            return False
