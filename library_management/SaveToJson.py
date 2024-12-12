import json
def save_to_json(file_name, data):
    """
    Saves data to the JSON file.

    Args:
    - file_name (str): The name of the JSON file.
    - data (dict): The data to be added to the file.
    """
    try:
        # Load data from JSON file
        with open(file_name, "r") as file:
            list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Initialize an empty list if the file doesn't exist or is invalid
        list = []

    # Append the new data to the list
    list.append(data)

    # Write the updated list back to the file
    with open(file_name, "w") as file:
        json.dump(list, file, indent=4)

def overwrite(file_name, data):
    """
    Overwrites the JSON file with the given data.

    Args:
    - file_name (str): The name of the JSON file.
    - data (list): The new data to overwrite the file with.
    """
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)