"""Manages the body frame setup and flow.

This module contains the BodyFrame class, which is responsible for setting up
the body frame in the main application window. The body frame contains a
notebook with tabs, each tab containing a scrollable canvas with checkboxes.

Classes:
    BodyFrame: Manages the body frame setup and flow.

Usage:
    Create an instance of the BodyFrame class with the required arguments to
    set up the body frame in the application window.
"""

# pylint: disable=unused-argument

import tkinter as tk
from tkinter import ttk
import os
from pyperclip import copy
from utils.load_data import load_task_data

class BodyFrame:
    """Manages the body frame setup and flow."""
    def __init__(self, root, data, directory, position: tuple):
        self.root = root
        self.data = data
        self.directory = directory # Link to create_body_frame to open correct file
        self.position = position

        # Create a Label with background color (For Debug purposes).
        # Change to Frame when done as label results in flickering
        self.label = tk.Label(self.root, background='blue')
        self.label.grid(row=self.position[0],
                        column=self.position[1],
                        columnspan=4,
                        sticky="nswe")

        self.body_frame_top = ()
        self.body_frame_bottom = ()

        self.load_frame()


    def load_frame(self):
        """
        Load the top and bottom frames.
        Destroy all widgets before reloading.
        """
        for element in self.body_frame_top[:]:
            if isinstance(element, dict):
                for tab, widgets in element.items():
                    for widget in widgets:
                        widget[0].destroy()
                    tab.destroy()
            else:
                element.destroy()
        
        for element in self.body_frame_bottom[:]:
            if isinstance(element, dict):
                for tab, widgets in element.items():
                    for widget in widgets:
                        widget[0].destroy()
                    tab.destroy()
            else:
                element.destroy()
        
        self.body_frame_top = self.create_body_frame(
            self.label, self.data
            )
        self.body_frame_bottom = self.create_body_frame(
            self.label, load_task_data("data/general.txt")
            )


    def create_body_frame(self, root, data):
        """Create a body frame"""
        body_frame = tk.Frame(root, highlightthickness=0)
        body_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, anchor="n")

        # Create the notebook.
        notebook = ttk.Notebook(body_frame)
        notebook.pack()

        # Dimensions of canvas.
        # Note that - 80 and +120)/4 are magic values and should be resolved.
        body_frame.update_idletasks()   # Ensure updated winfo is obtained.
        width = self.root.winfo_width() - 80
        height = (self.root.winfo_height() + 120)/4

        widgets = {}    # {tab: [label, ...], ...}
        canvas_and_inner_frame = {} # {body_frame: (canvas, inner_frame), ...}  <--- Looks inefficient

        for heading, content in data.items():
            # Create the tabs in the notebook.
            tab = tk.Frame(notebook, highlightthickness=0)
            text = f"{heading[:4]}..." if len(heading) > 4 else heading
            notebook.add(tab, text=text)

            # Create a canvas with inner_frame for scrollbar.
            canvas, inner_frame = self.create_scrollable_canvas(
                tab, width, height
                )

            canvas_and_inner_frame[body_frame] = (canvas, inner_frame)

            # Create checkboxes.
            checkboxes = []
            for text in content:
                var = tk.BooleanVar()
                label = tk.Checkbutton(inner_frame, text=text[0], variable=var)
                checkboxes.append((label, var))
                label.pack(side="top", anchor="nw")
            widgets[tab] = checkboxes

            # Make each canvas scrollable.
            inner_frame.bind(
                "<Configure>",
                lambda event,
                canvas=canvas_and_inner_frame[body_frame][0]: self.enable_scroll(
                    event,
                    canvas
                    ))
            inner_frame.bind_all("<MouseWheel>", self.scroll_on_mousewheel)

        # Create button for opening task file.
        button = ttk.Button(body_frame,
                            text="Open",
                            width=5,
                            command=self.open_file)
        button.pack(side="right", anchor="ne")

        # Create button for copying selected boxes.
        button = ttk.Button(body_frame,
                            text="Copy",
                            width=5,
                            command=self.copy_to_clipboard)
        button.pack(side="right", anchor="ne")

        # Returns all widgets created in the method.
        return (inner_frame, canvas, notebook, body_frame, widgets)


    def create_scrollable_canvas(self, parent, width, height):
        """Create a scrollable canvas."""
        canvas = tk.Canvas(parent,
                           width=width,
                           height=height,
                           highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(parent, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)
        return canvas, inner_frame


    def enable_scroll(self, event, canvas):
        """Enables scroll."""
        canvas.configure(scrollregion=canvas.bbox("all"))


    def get_canvas(self, widget_name):
        """Get the canvas widget that a given widget is on."""
        widget = self.root.nametowidget(widget_name)
        parent = widget

        # Cycles through the widget that was scrolled on to determine if
        # it lies on a canvas.
        while parent:
            parent = self.root.nametowidget(parent)
            if isinstance(parent, tk.Canvas):
                return parent

            # Cycle up the layer of widgets.
            parent = parent.winfo_parent()

        # If mouse scroll did not occur on a widget that lies on a
        # canvas.
        return None


    def scroll_on_mousewheel(self, event):
        """Scroll the canvas."""
        canvas_widget = self.get_canvas(event.widget)
        if canvas_widget:
            if canvas_widget.winfo_height() < canvas_widget.bbox("all")[3]:
                canvas_widget.yview_scroll(-1 * (event.delta // 120), "units")


    def open_file(self, event=None):
        """Open the data folder."""
        file_path = os.path.join(os.getcwd(), self.directory)
        os.system(f'start "" "{file_path}"')


    def copy_to_clipboard(self, event=None):
        """Copy data of selected checkboxes to clipboard"""
        selected_tab_frame = self.body_frame_top[2].select()
        selected_tab_index = self.body_frame_top[2].index(selected_tab_frame)
        selected_tab_key = list(self.body_frame_top[4].keys())[selected_tab_index]
        selected_tab_text = [value for _, value in self.data.items()][selected_tab_index]
        selected_tab = self.body_frame_top[4][selected_tab_key]

        text = []
        for i, _checkbox in enumerate(selected_tab):
            if _checkbox[1].get():
                text.append(selected_tab_text[i][1])
                _checkbox[1].set(False)

        text = "\n".join(text)
        copy(text)
        print(text)
