#!/usr/bin/env python3
"""
AstraTerm AI Launcher Script
Run this script to start AstraTerm without installation
"""

import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Import and run the application
try:
    from astraterm.main import run_app
    
    if __name__ == "__main__":
        print("Starting AstraTerm AI v1.2.0...")
        print("Press Ctrl+Q to quit\n")
        run_app()
except ImportError as e:
    print(f"Error: Missing dependencies - {e}")
    print("\nPlease install required packages:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\nGoodbye!")
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
