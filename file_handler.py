import json
import os

FILE_NAME = "todo.json"


def load_tasks():
    """
    Load tasks from the JSON file.
    Returns an empty list if the file doesn't exist or is invalid.
    """
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """
    Save the list of tasks to the JSON file.
    """
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)