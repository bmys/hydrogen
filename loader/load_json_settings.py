import json


def load_setting(file_name):
    settings = None
    with open(file_name) as file:
        return json.load(file)


