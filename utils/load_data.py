"""Module for loading data from text files into a nested dictionary structure.

This module contains functions for loading data from text files into a nested
dictionary structure. The data in the text files is formatted to represent tabs
and checkboxes, which are then stored in the dictionary.

Functions:
    load_task_data: Load data from a file into a nested dictionary.
    format_label: Format label by removing keywords and hashtags.

Usage:
    Use the load_task_data function to load data from a text file into a
    nested dictionary. The format_label function can be used to format
    labels by removing keywords and hashtags.
"""

import os


def load_task_data(directory:str) -> dict:
    """
    Load data from a file into a nested dictionary.

    Args:
    - directory (str): The directory path of the file.

    Returns:
    - dict: A nested dictionary containing the loaded data.
    """

    # Ensure that there is a valid file at directory.
    if not os.path.isfile(directory):
        return {
            "ERROR": [
                (f"Invalid file at '{directory}'","Not a valid directory")
                ]
            }

    data_dict = {}

     # Track if a tab or checkbox is being processed.
    tab = False
    checkbox = False

    # Store the current tab and checkbox labels.
    tab_label = ""
    checkbox_label = ""

    # Store checkbox items and text lines.
    checkboxes = []
    text = []

    # Extract information from given txt file.
    with open(directory, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            # Check if the line indicates a new tab.
            if line.startswith("# tab"):
                if not tab:
                    # Save the tab label.
                    tab_label = format_label(line[5:])
                else:
                    # Save the checkboxes under the previous tab.
                    data_dict[tab_label] = checkboxes
                    checkboxes = []
                tab = not tab
                continue

             # Check if the line indicates a new checkbox.
            if tab and line.startswith("# checkbox", 4):
                if not checkbox:
                    # Save the checkbox label
                    checkbox_label = format_label(line[14:])
                else:
                    # Save the checkbox text under the previous checkbox.
                    checkboxes.append(
                        (checkbox_label, "\n".join(x for x in text))
                        )
                    text = []
                checkbox = not checkbox
                continue

            if tab and checkbox:
                # Save the checkbox text.
                text.append(line[8:].strip("\n"))

    return ensure_data_integrity(data_dict)


def ensure_data_integrity(data):
    """
    Ensure that each item in the given data is of the format:
    {string: list of tuples containing two values}

    Args:
    - data (dict): the dictionary to check.

    Returns:
    - dict: "data" if valid, else {"ERROR": [("Invalid file format", "")]}
    """
    for key, value in data.items():
        if not (isinstance(key, str) and key != "" and isinstance(value, list) and len(value) > 0):
            return {"ERROR": [("Invalid file format", "")]}
        for type_tuple in value:
            if not (isinstance(type_tuple, tuple) and len(type_tuple) == 2 and type_tuple[0] != "" and type_tuple[1] != ""):
                return {"ERROR": [("Invalid file format", "")]}
    return data



def format_label(label:str) -> str:
    """Format label by removing keywords and hashtags"""
    return " ".join(word for word in label.strip(" ").split())


if __name__ == "__main__":
    # Test for valid files in data directory.
    test_data = load_task_data("data\\buttons.txt")
    for _key, _value in test_data.items():
        print("Output 1: ", "{", f"{_key}: ", _value, "}", sep="")
    print("-"*10)

    # Test for valid files in data/* directory.
    test_data = load_task_data("data\\test_file_1.txt")
    for _key, _value in test_data.items():
        print("Output 2: ", "{", f"{_key}: ", _value, "}", sep="")
    print("-"*10)

    # Test for invalid files.
    test_data = load_task_data("data\\invalid_file.txt")
    for _key, _value in test_data.items():
        print("Output 3: ", "{", f"{_key}: ", _value, "}", sep="")
    print("-"*10)

    # Test for invalid directories.
    test_data = load_task_data("data")
    for _key, _value in test_data.items():
        print("Output 4: ", "{", f"{_key}: ", _value, "}", sep="")
