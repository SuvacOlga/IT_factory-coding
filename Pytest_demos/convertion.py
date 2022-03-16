import json

import json2xml.dicttoxml
from json2html import *
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

json_file_path = 'C:\\Users\\Moldoveanu\\Documents\\GitHub\\IT_Factory_Course\\src\\home_work\\part_2_automation\\report\\ceebb497-4d01-4336-a2f9-a428e0a6eed8-result.json'
with open(json_file_path) as file:
    json_data = json.load(file)

html_file_path = 'C:\\Users\\Moldoveanu\\Documents\\GitHub\\IT_Factory_Course\\src\\home_work\\part_2_automation\\report\html_report.html'
html_data = json2html.convert(json=json_data)
with open(html_file_path, 'w') as file:
    file.write(html_data)

# xml_file_path = 'C:\\Users\\Moldoveanu\\Documents\\GitHub\\IT_Factory_Course\\src\\part_2_automation\\report\\xml_report.xml'
# xml_data = json2xml.Json2xml(json_data).to_xml()
# with open(xml_file_path, 'w') as file:
#     file.write(xml_data)
