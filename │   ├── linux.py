# astraterm/linux.py
import subprocess

class LinuxDistro:
    def __init__(self, distro: str = "kali"):
        self.distro = distro

    def install(self):
        subprocess.run(["proot-distro", "install", self.distro])

    def start(self):
        subprocess.run(["proot-distro", "login", self.distro])
