"""Module for managing the footer frame setup and flow.

This module contains the FooterFrame class, which is responsible for setting up
the footer frame in the main application window. The footer frame contains a
button for opening the data folder.

Classes:
    FooterFrame: Manages the footer frame setup and flow.

Usage:
    Create an instance of the FooterFrame class with the required arguments to
    set up the footer frame in the application window.
"""

import os
import tkinter as tk
from tkinter import ttk


class FooterFrame:
    """Manages the footer frame setup and flow."""
    def __init__(self, root, data, position:tuple):
        self.root = root
        self.data = data

        # Create a Label with background color (For Debug purposes).
        self.label = tk.Label(self.root, background='black')
        self.label.grid(row=position[0], column=position[1], columnspan=4, sticky="swe")
        style = ttk.Style()
        style.configure("footer_frame.TButton", background="black")

        self.open_folder_button = self.create_open_folder_button()

    def create_open_folder_button(self):
        """Create a button for opening the data folder."""
        button = ttk.Button(self.label,
                            text="Open Data Folder",
                            width=16,
                            style="footer_frame.TButton",
                            command=self.open_folder)
        button.pack(side="right", anchor="e")
        return button


    def open_folder(self, event=None):
        """Open the data folder"""
        data_directory = fr"{os.getcwd()}\data"
        os.system(f"start explorer {data_directory}")
