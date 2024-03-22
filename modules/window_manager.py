"""Module for managing the main application setup and flow.

This module contains the WindowManager class, which is responsible for
setting up the main Tkinter application window and managing its frames.

Classes:
    WindowManager: Manages the main application setup and flow.

Usage:
    Run this module to start the application.
"""

import tkinter as tk
from modules.side_frame import SideFrame
from modules.header_frame import HeaderFrame
from modules.footer_frame import FooterFrame
from modules.body_frame import BodyFrame
from utils.load_data import load_task_data

class WindowManager:
    """Manages the main application setup and flow."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.minsize(100, 100)
        self.root.overrideredirect(True)
        self.root.bind("<Return>", self.get_body_data)

        self.screen_width = self.root.winfo_screenwidth()
        self.root.geometry(f"300x500+{self.screen_width - 300}+100")

        self.frames = []
        self.active_directory = "data"

        self.create_frames()

    def create_frames(self):
        """Creates the application frames."""
        default_side_data =  load_task_data("data/buttons.txt")
        default_body_data = load_task_data("data/task_1.txt")
        
        # Create frames.
        self.frames.append(HeaderFrame(self.root, (0, 0)))
        self.frames.append(SideFrame(self.root, default_side_data, (1, 0)))
        self.frames.append(BodyFrame(self.root, default_body_data, "data/test_file_1.txt", (1,1)))
        self.frames.append(FooterFrame(self.root, [], (1, 0)))

        self.active_directory = self.frames[0].directory_field.get()
        print(self.active_directory)

        # Ensure that frames take up the entire area of the window.
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.root.mainloop()

    def get_body_data(self, event):
        """Gets data for the body frame."""
        self.active_directory = self.frames[0].directory_field.get()
        self.frames[2].data = load_task_data(self.active_directory)
        self.frames[2].directory = self.active_directory
        self.frames[2].load_frame()
