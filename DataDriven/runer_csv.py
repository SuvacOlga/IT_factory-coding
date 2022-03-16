import os

from src.part_2_automation.data_driven.runner import my_test_case
from src.part_2_automation.data_driven.parser_csv_file import get_input_data_csv

# csv running test
data_csv = get_input_data_csv(os.getcwd() + '/input_data/input_data_csv.txt')

for x in data_csv:
    status = my_test_case(x[0], x[1])
    print(status)
