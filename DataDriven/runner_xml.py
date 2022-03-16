import os

from src.part_2_automation.data_driven.runner import my_test_case
from src.part_2_automation.data_driven.parser_xml_file import get_input_data_xml

# xml running test
data_xml = get_input_data_xml(os.getcwd() + '/input_data/input_data_xml.xml')

for x in data_xml.findall('tc'):
    status = my_test_case(x.find('input').text, x.find('expected').text)
    print(status)
