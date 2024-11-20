import os
import json

def read_json_file(filepath):
    """
    Reads a JSON file and returns its contents as a Python object.

    Args:
        filepath (str): The path to the JSON file to be read.

    Returns:
        dict: A dictionary containing the contents of the JSON file.
        None: If the file doesn't exist
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None

def write_json_file(filepath, data):
    """
    Write data to a JSON file at the specified filepath.

    Args:
        filepath (str): The path to the file to write.
        data (dict): The data to write to the file.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def append_json_file(filepath, data):
    """
    Append data to a JSON file at the specified filepath.

    Args:
        filepath (str): The path to the file to write.
        data (dict): The data to write to the file.

    Returns:
        None
    """
    
    try:
        oldData = read_json_file(filepath)
        if oldData is None:
            oldData = []
    except:
        oldData = []
 
    oldData.append(data)

    write_json_file(filepath, oldData)

def delete_file(filepath):
    """
    Deletes a file at the specified filepath.

    Args:
        filepath (str): The path to the file to delete.

    Returns:
        None
    """
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass