# TaskManager

This application provides a toolkit for reviewing text data organized into tasks and categories. It allows users to view and copy text data associated with different tasks and categories. Users can also reload data and open files from within the application.

## Installation

### Method 1
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/review-toolkit.git
   ```
2. Install the required dependencies:
   - Python 3.x
   - `tkinter` (for GUI)
   - `pyperclip` (for clipboard operations)
3. Run the application by executing the `ReviewToolkit` class.

### Method 2 (No dependencies needs to be considered)

1. Download the files in the "distr" folder.
2. Copy "data" folder directly into _internal folder.
3. Run executable.

## File Structure

- `main.py`: Main entry point of the application.
- `modules/`: Directory containing modules for different parts of the application.
  - `__init__.py`: Python package initialization file.
  - `body_frame.py`: Manages the body frame setup and flow.
  - `footer_frame.py`: Manages the footer frame setup and flow.
  - `header_frame.py`: Manages the header frame setup and flow.
  - `side_frame.py`: Manages the side frame setup and flow.
  - `window_manager.py`: Manages the main application setup and flow.
- `utils/load_data.py`: Contains functions for loading data from text files.
- `data/`: Directory for storing data files used by the application.

## Usage

1. Run main.py to initialize the application.
2. The application window will display tabs for each task, with checkboxes for different criteria under each task.
3. Check the boxes for the criteria you want to copy to the clipboard.
4. Click the "Copy" button to copy the selected criteria to the clipboard.
5. Click the "Open" button to open the selected tab's text file.
6. Navigate to a file in the field on top.

## Example Data

The application works with text files organized in a specific format. See the example data format in the `data` directory.

## Modules

### main.py
**Purpose:** The main entry point of the application.  
**Dependencies:** Requires `os` and `tkinter` modules.  
**Usage:** Run this script to start the application.

---

### window_manager.py
**Purpose:** Manages the main application setup and flow.  
**Dependencies:** Depends on `tab_manager`, `frame_manager`, `load_data`, and `constants` modules.  
**Classes:**
- **WindowManager:** Manages the main application setup and flow.  
**Usage:** Instantiate `WindowManager` with a `tk.Tk()` instance to set up the application.

---

### tab_manager.py
**Purpose:** Manages the creation and handling of tabs.  
**Dependencies:** Depends on `frame_manager` module.  
**Classes:**
- **TabManager:** Manages the creation and handling of tabs.  
**Usage:** Instantiate `TabManager` with a `tk.Tk()` instance to create tabs within the application.

---

### frame_manager.py
**Purpose:** Manages the creation and handling of frames.  
**Dependencies:** Depends on `button_manager` and `checkbox_manager` modules.  
**Classes:**
- **FrameManager:** Manages the creation and handling of frames.  
**Usage:** Instantiate `FrameManager` with a `tk.Tk()` instance to create frames within the application.

---

### button_manager.py
**Purpose:** Manages the creation and handling of buttons within frames.  
**Dependencies:** Depends on `pyperclip` module.  
**Classes:**
- **ButtonManager:** Manages the creation and handling of buttons within frames.  
**Usage:** Instantiate `ButtonManager` with a parent widget, file name, action type, position tuple, and data dictionary to create a button within a frame.

---

### checkbox_manager.py
**Purpose:** Manages the creation and handling of check buttons within tabs.  
**Dependencies:** None.  
**Classes:**
- **CheckboxManager:** Manages the creation and handling of check buttons within tabs.  
**Usage:** Instantiate `CheckboxManager` with a parent widget, file name, data dictionary, and position tuple to create a check button within a tab.

---

### load_data.py
**Purpose:** Loads data from text files into a nested dictionary.  
**Dependencies:** None.  
**Functions:**
- `load_task_data(directory)`: Loads data from text files into a nested dictionary.  
**Usage:** Call `load_task_data(directory)` with a directory path to load data from text files into a nested dictionary.

## License

Copyright (c) 2024 kader-the-coder

The full text of the license can be found [here](./LICENSE).
