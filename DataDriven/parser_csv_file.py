import csv


def get_input_data_csv(file_name):
    csv_reader = csv.reader(file_name)
    return csv_reader
