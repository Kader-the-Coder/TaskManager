"""Module for managing the side frame setup and flow.

This module contains the SideFrame class, which is responsible for setting up
the side frame in the main application window. The side frame contains buttons
that can copy text to the clipboard.

Classes:
    SideFrame: Manages the side frame setup and flow.

Usage:
    Create an instance of the SideFrame class with the required arguments to
    set up the side frame in the application window.
"""

import tkinter as tk
from tkinter import ttk
from pyperclip import copy

class SideFrame:
    """Manages the side frame setup and flow."""
    def __init__(self, root, data: list, position: tuple):
        self.root = root
        self.data = data["buttons"]

        # Create a Label with background color (For Debug purposes).
        self.label = tk.Frame(self.root, background='yellow')
        self.label.grid(row=position[0],
                        column=position[1],
                        columnspan=1,
                        sticky="wns")

        # Create buttons.
        self.quick_copy_buttons = [self.create_button(text[0], text[1])
                                   for text in self.data]


    def create_button(self, button_label, text_to_copy):
        """Create a button which copies its text to clipboard"""
        button = ttk.Button(self.label,
                            text=button_label,
                            width=3,
                            style="side_frame.TButton",
                            command=lambda: self.copy_to_clipboard(text_to_copy))
        button.pack(side="top", anchor="e")
        return button


    def copy_to_clipboard(self, text, event=None):
        """Copy text of button to clipboard"""
        copy(text)
