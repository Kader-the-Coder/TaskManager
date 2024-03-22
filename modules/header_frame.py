"""Module for managing the header frame setup and flow.

This module contains the HeaderFrame class, which is responsible for setting up
the header frame in the main application window. The header frame contains
buttons for showing/hiding the window, entering a directory path, and closing
the application.

Classes:
    HeaderFrame: Manages the header frame setup and flow.

Usage:
    Create an instance of the HeaderFrame class with the required arguments to
    set up the header frame in the application window.
"""

import tkinter as tk
from tkinter import ttk

class HeaderFrame:
    """Manages the header frame setup and flow."""
    def __init__(self, root, position:tuple):
        self.root = root
        self.geometry = root.geometry() # Store geometry for show/hide button.
        self.position = position
        self.selected_directory = ""
        self.hidden = False

        # Create a Label with background color (For Debug purposes).
        self.label = tk.Frame(self.root, background='red')
        self.label.grid(row=position[0], column=position[1], columnspan=4, sticky="nwe")
        style = ttk.Style()
        style.configure("header_frame.TButton", background="red")
        style.configure('header_frame.TEntry', padding=(2, 2))
        style.configure('header_frame.TEntry', borderwidth=100)

        # Create buttons.
        self.show_hide_button = self.create_show_hide_button()
        self.directory_field = self.create_directory_field()
        self.close_button = self.create_close_button()
        

    def create_show_hide_button(self):
        """Create a button for showing or hiding the window."""
        show_hide_button = ttk.Button(self.label,
                                      text="<>",
                                      width=3,
                                      style="header_frame.TButton",
                                      command=self.show_hide)
        show_hide_button.pack(side="left")
        # Enable user to drag the window by holding down the mouse button.
        show_hide_button.bind("<B1-Motion>", self.drag_window)
        return show_hide_button


    def create_directory_field(self):
        """Create an entry field for entering a directory path."""
        directory_field = ttk.Entry(self.label,
                                    cursor="ibeam",
                                    width=20,
                                    style="header_frame.TEntry")
        directory_field.insert(0, "data\\")
        directory_field.bind("<Return>", self.get_directory)
        directory_field.pack(side="left", padx=4)
        return directory_field

    def create_close_button(self):
        """Create a button for closing the application."""
        show_hide_button = ttk.Button(self.label,
                                      text="X",
                                      width=5,
                                      style="header_frame.TButton",
                                      command=self.close_application)
        show_hide_button.pack(side="right")
        return show_hide_button


    def close_application(self, event=None):
        """Close the application, effectively ending this program"""
        self.root.destroy()


    def drag_window(self, event=None):
        """
        Changes the y position of the window based on mouse position
        if the window is not set hidden.
        """
        if not self.hidden:
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            screen_width = self.root.winfo_screenwidth()
            x_position = screen_width - width
            # Adjust the y position based on the mouse position
            y_position = event.y_root
            self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
            self.geometry = self.root.geometry()


    def show_hide(self, event=None):
        """Shows or hides the window."""
        self.hidden = not self.hidden
        # Get current dimensions of root window.
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        # Get the screen width.
        screen_width = self.root.winfo_screenwidth()
        # Calculate the new x-coordinate to position the window at.
        
        # Temporary Brute force method to get window position to update.
        if self.hidden:
            x_position = screen_width - width
            while x_position < screen_width - round(width/10):
                # Calculate the new x-coordinate to position the window at.
                x_position += 1
                # Set the new geometry of the root window
                self.root.geometry(
                    f"{width}x{height}+{x_position}+{self.root.winfo_y()}"
                    )
                self.root.update_idletasks()  # Update the window immediately
        else:
            x_position = screen_width - round(width/10)
            while x_position > screen_width - width:
                # Calculate the new x-coordinate to position the window at.
                x_position -= 1
                # Set the new geometry of the root window
                self.root.geometry(
                    f"{width}x{height}+{x_position}+{self.root.winfo_y()}"
                    )
                self.root.update_idletasks()  # Update the window immediately

        self.geometry = self.root.geometry()


    def get_directory(self, event=None):
        """Returns the text in the entry field"""
        self.selected_directory = self.directory_field.get()
        print(self.selected_directory)


if __name__ == "__main__":
    # Set up paths for unit testing.
    import os
    import sys
    parent_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(parent_folder)

    test_root = tk.Tk()
    test_root.geometry("200x100")
    test_data = ["x", "y", "z"]
    test_position = (0, 1)
    HeaderFrame(test_root, test_position)
    test_root.mainloop()
