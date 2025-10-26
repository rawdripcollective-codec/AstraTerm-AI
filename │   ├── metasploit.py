# astraterm/metasploit.py
import subprocess

class Metasploit:
    def install(self):
        subprocess.run(["apt", "install", "-y", "metasploit-framework"])

    def run_console(self):
        subprocess.run(["msfconsole"])
