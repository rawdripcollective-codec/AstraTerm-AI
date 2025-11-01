#!/usr/bin/env python3
"""
Project Verification Script for AstraTerm AI
Checks if all files are properly configured and ready to run
"""

import sys
from pathlib import Path
import importlib.util

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if filepath.exists():
        print(f"✓ {description}: {filepath.name}")
        return True
    else:
        print(f"✗ {description}: {filepath.name} - NOT FOUND")
        return False

def check_python_syntax(filepath):
    """Check if Python file has valid syntax"""
    try:
        with open(filepath, 'r') as f:
            compile(f.read(), filepath, 'exec')
        return True
    except SyntaxError as e:
        print(f"  ✗ Syntax error in {filepath.name}: {e}")
        return False

def check_module_import(module_name):
    """Check if a module can be imported"""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is not None:
            print(f"✓ Module '{module_name}' can be imported")
            return True
        else:
            print(f"✗ Module '{module_name}' not found")
            return False
    except Exception as e:
        print(f"✗ Error importing '{module_name}': {e}")
        return False

def main():
    print("=" * 60)
    print("AstraTerm AI - Project Verification")
    print("=" * 60)
    print()
    
    project_root = Path(__file__).parent
    astraterm_dir = project_root / "astraterm"
    
    all_checks_passed = True
    
    # Check project structure
    print("1. Checking Project Structure...")
    print("-" * 60)
    
    required_files = [
        (project_root / "README.md", "README file"),
        (project_root / "setup.py", "Setup file"),
        (project_root / "requirements.txt", "Requirements file"),
        (project_root / "config.json", "Config template"),
        (astraterm_dir / "__init__.py", "Package init"),
    ]
    
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    print()
    
    # Check Python modules
    print("2. Checking Python Modules...")
    print("-" * 60)
    
    modules = [
        "main.py",
        "config.py",
        "terminal.py",
        "ai_assistant.py",
        "github.py",
        "linux.py",
        "metasploit.py",
        "nmap.py",
        "osint.py",
        "plugins.py",
        "resources.py",
    ]
    
    for module in modules:
        module_path = astraterm_dir / module
        if module_path.exists():
            print(f"✓ {module}")
            if not check_python_syntax(module_path):
                all_checks_passed = False
        else:
            print(f"✗ {module} - NOT FOUND")
            all_checks_passed = False
    
    print()
    
    # Check Python version
    print("3. Checking Python Environment...")
    print("-" * 60)
    
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version >= (3, 8):
        print("✓ Python version is compatible (>= 3.8)")
    else:
        print("✗ Python version is too old (requires >= 3.8)")
        all_checks_passed = False
    
    print()
    
    # Check dependencies (optional)
    print("4. Checking Dependencies (Optional)...")
    print("-" * 60)
    
    optional_modules = [
        "textual",
        "rich",
        "requests",
    ]
    
    for module in optional_modules:
        check_module_import(module)
    
    print()
    
    # Summary
    print("=" * 60)
    if all_checks_passed:
        print("✓ All critical checks passed!")
        print()
        print("Next steps:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Configure API keys in config.json")
        print("  3. Run the application: python3 run.py")
        print("     or install: pip install -e .")
        print("     then run: astraterm")
        return 0
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
