"""
main.py: Entry point for the application.

This script sets the current working directory to the directory containing
the script, then creates an instance of the WindowManager class from the 
modules.window_manager module.

Usage:
    Run this script to start the application.
"""

import os
from modules.window_manager import WindowManager

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    app = WindowManager()
