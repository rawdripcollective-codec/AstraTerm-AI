# astraterm/resources.py
import requests
import subprocess
import shutil
from typing import Optional, Dict
from pathlib import Path

class ResourceUpdater:
    """Manage resources, cheat sheets, and library installations"""
    
    CHEAT_SHEET_SOURCES = {
        "python": "https://raw.githubusercontent.com/gto76/python-cheatsheet/main/README.md",
        "bash": "https://devhints.io/bash",
        "git": "https://training.github.com/downloads/github-git-cheat-sheet.pdf",
        "docker": "https://raw.githubusercontent.com/wsargent/docker-cheat-sheet/master/README.md",
        "kubernetes": "https://kubernetes.io/docs/reference/kubectl/cheatsheet/",
    }
    
    def __init__(self, cache_dir: str = ".astraterm/cache"):
        self.cache_dir = Path.home() / cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch_cheat_sheet(self, lang: str) -> str:
        """
        Fetch cheat sheet for a programming language or tool
        
        Args:
            lang: Language or tool name
        
        Returns:
            Cheat sheet content or error message
        """
        lang = lang.lower()
        
        # Check cache first
        cache_file = self.cache_dir / f"{lang}_cheatsheet.txt"
        if cache_file.exists():
            try:
                return cache_file.read_text()
            except Exception:
                pass
        
        # Fetch from source
        if lang in self.CHEAT_SHEET_SOURCES:
            try:
                response = requests.get(self.CHEAT_SHEET_SOURCES[lang], timeout=10)
                if response.ok:
                    content = response.text
                    # Cache the content
                    try:
                        cache_file.write_text(content)
                    except Exception:
                        pass
                    return content
                return f"Error fetching cheat sheet: HTTP {response.status_code}"
            except Exception as e:
                return f"Error fetching cheat sheet: {str(e)}"
        else:
            # Generate basic cheat sheet
            return self._generate_basic_cheatsheet(lang)

    def _generate_basic_cheatsheet(self, lang: str) -> str:
        """Generate a basic cheat sheet for common languages"""
        cheatsheets = {
            "python": """Python Cheat Sheet:
# Variables
x = 5
name = "AstraTerm"

# Functions
def greet(name):
    return f"Hello, {name}!"

# Lists
my_list = [1, 2, 3, 4, 5]

# Loops
for item in my_list:
    print(item)

# Conditionals
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
""",
            "javascript": """JavaScript Cheat Sheet:
// Variables
let x = 5;
const name = "AstraTerm";

// Functions
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrays
const myArray = [1, 2, 3, 4, 5];

// Loops
for (let item of myArray) {
    console.log(item);
}

// Conditionals
if (x > 0) {
    console.log("Positive");
} else if (x < 0) {
    console.log("Negative");
} else {
    console.log("Zero");
}
""",
            "bash": """Bash Cheat Sheet:
# Variables
name="AstraTerm"
x=5

# Functions
greet() {
    echo "Hello, $1!"
}

# Loops
for i in {1..5}; do
    echo $i
done

# Conditionals
if [ $x -gt 0 ]; then
    echo "Positive"
elif [ $x -lt 0 ]; then
    echo "Negative"
else
    echo "Zero"
fi
"""
        }
        
        return cheatsheets.get(lang, f"Cheat sheet for {lang}: Not available yet")

    def install_lib(self, lib: str, package_manager: str = "pip") -> bool:
        """
        Install a library using specified package manager
        
        Args:
            lib: Library name
            package_manager: Package manager (pip, npm, apt, etc.)
        
        Returns:
            True if installation successful, False otherwise
        """
        if not shutil.which(package_manager):
            print(f"Package manager '{package_manager}' not found")
            return False
        
        try:
            if package_manager == "pip":
                cmd = ["pip", "install", lib]
            elif package_manager == "npm":
                cmd = ["npm", "install", "-g", lib]
            elif package_manager == "apt":
                cmd = ["apt", "install", "-y", lib]
            elif package_manager == "cargo":
                cmd = ["cargo", "install", lib]
            else:
                cmd = [package_manager, "install", lib]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            if result.returncode == 0:
                print(f"Successfully installed {lib}")
                return True
            else:
                print(f"Failed to install {lib}: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            print(f"Installation of {lib} timed out")
            return False
        except Exception as e:
            print(f"Error installing {lib}: {str(e)}")
            return False

    def update_resources(self) -> bool:
        """Update all cached resources"""
        try:
            for lang in self.CHEAT_SHEET_SOURCES.keys():
                cache_file = self.cache_dir / f"{lang}_cheatsheet.txt"
                if cache_file.exists():
                    cache_file.unlink()
                self.fetch_cheat_sheet(lang)
            return True
        except Exception as e:
            print(f"Error updating resources: {str(e)}")
            return False

    def clear_cache(self) -> bool:
        """Clear all cached resources"""
        try:
            for file in self.cache_dir.glob("*"):
                if file.is_file():
                    file.unlink()
            return True
        except Exception as e:
            print(f"Error clearing cache: {str(e)}")
            return False
