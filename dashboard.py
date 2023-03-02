import json
import pandas as pd

# Reads and returns the contents of a JSON file
def read_json(file_name: str):
    with open(file_name, 'rt') as file:
        return json.load(file) 

# Extracts and returns the data of a JSON file
def extract_data(file_name: str):
    data = read_json(file_name)
    return data['items']

dataset = extract_data('ons.json')
for line in dataset:
    print(line['title'])