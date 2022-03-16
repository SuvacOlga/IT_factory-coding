import os
from fuzzywuzzy import fuzz

from src.part_2_automation.data_driven.parser import get_input_data
from src.part_2_automation.data_driven.parser_csv_file import get_input_data_csv



def my_test_case(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)

    if similarity > 90:
        print("passed")
    elif 30 < similarity < 90:
        print('warning')
    else:
        print('not pass')

    return similarity


# print(os.getcwd())
data = get_input_data(os.getcwd() + '/input_data/input_data.json')

for key, value in data.items():
    # print(key, value)
    status = my_test_case(data[key]['input'], data[key]['expected'])
    print(status)
