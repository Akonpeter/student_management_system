import json
import os

def load_data(filename):
    """
    Load data from a JSON file.
    Returns an empty list if the file does not exist
    or contains invalid JSON.
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    



    # Save_data function

def save_data(filename, data):
    """
    Save data to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)    