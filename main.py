"""
main.py: Entry point for the application.

This script sets the current working directory to the directory containing
the script, then creates an instance of the WindowManager class from the 
modules.window_manager module.

Usage:
    Run this script to start the application.
"""

import os
import json
from modules.window_manager import WindowManager

if __name__ == "__main__":
    # Set directory to working directory.
    os.chdir(os.path.dirname(__file__))

    # Load config data.
    config_file_path = "data/config.json"

    try:
        with open(config_file_path, "r", encoding="utf-8") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        config_data = {
            "default_active_directory": "data",
            "default_side_data": "data/buttons.txt",
            "default_body_data": "data/general.txt"
        }
        with open(config_file_path, "w", encoding="utf-8") as config_file:
            json.dump(config_data, config_file, indent=4)

    app = WindowManager(config_data)
