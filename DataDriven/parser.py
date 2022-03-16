import json


def get_input_data(file_name):
    json_file = open(file_name)
    return json.load(json_file)
