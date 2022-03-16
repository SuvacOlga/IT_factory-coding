import xml.etree.ElementTree as ET


def get_input_data_xml(file_name):
    mytree = ET.parse(file_name)
    myroot = mytree.getroot()
    return myroot
