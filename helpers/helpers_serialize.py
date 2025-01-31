import json
import os.path
from typing import Dict

import toml
import yaml

def get_serialized_data(path: str) -> Dict:
    """
    Reads and deserializes data from file based on its extension. Supported formats are YAML, JSON and TOML.

    This function opens the files at the specified path identifies, its extension, and deserializes its content
        into a Python dictionary or list (depending on the format). The following file extensions are supported:
        - '.yaml' or '.yml' (YAML format)
        - '.json' (JSON format)
        - '.toml' (TOML format)

    If the file extension is unsupported, a ValueError is raised.

    :param path: The file path of the deserialized data to be loaded.
                    This must be a valid path to the file with a supported extension (.yaml, .yml, .json, .toml).

    :return: A Python dictionary or list containing the deserialized data.
            The return type depends on the content of the file (e.g., a dictionnary for JSON and TOML, a dictionnary or a list for YAML).

    :raises ValueError: If the file extension is not supported or the file cannot be opened.
    """

    _, extension= os.path.splitext(path)

    with open(path, 'r') as file:
        if extension == '.yaml':
            return yaml.safe_load(file)
        elif extension == '.json':
            return json.load(file)
        elif extension == '.toml':
            return toml.load(file)

        raise ValueError(f'Unsupported file extension {extension} | file={path}.')


def dict_to_deserialized_file(data: dict, path: str) -> None:
    """
    Serializes a Python dictionary and writes it to file in a specified format.

    This function take a dictionary and writes it to a file at the given path. The file's extension determines
    the format of the serialized data. Supported formats include:
    - YAML (.yaml or .yml)
    - JSON (.json)
    - TOML (.toml)

    The function will raise a 'ValueError' if the file extension is unsupported.

    :param data: The Python dictionary to be serialized and writen to the file.
    :param path: The file path where the serialized data will be saved.
                    The file extension determines the format of the serialized data.
                    Supported extensions : .yaml, .json, .toml.
    :raise ValueError: If the file extension is not supported.
    """
    _, extension = os.path.splitext(path)
    if extension == '.yaml':
        yaml.dump(data, file)
    elif extension == '.json':
        json.dump(data, file, indent=4)
    elif extension == '.toml':
        toml.dump(data,file)
    else:
        raise ValueError(f'Unsupported file extension {extension} | file={path}.')
