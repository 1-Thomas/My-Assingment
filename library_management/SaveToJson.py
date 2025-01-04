import json
def save_to_json(file_name, data):
    """
    Saves data to the JSON file.

    Args:
    - file_name (str): The name of the JSON file.
    - data (dict): The data to be added to the file.
    """
    #Reads the JSON file
    try:
        with open(file_name, "r") as file:
            list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        list = []

    # Append the data to list
    list.append(data)

    # Write back to file
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