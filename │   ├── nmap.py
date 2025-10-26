# astraterm/nmap.py
import nmap

class NmapScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan(self, target: str, args: str = "-sV -sC"):
        self.nm.scan(target, arguments=args)
        return self.nm.all_hosts()
