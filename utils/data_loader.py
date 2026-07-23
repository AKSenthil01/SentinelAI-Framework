import json

def load_test_data():
    #with open("data_generator/data_generator.json") as f:
    with open("test_data/test_data.json") as f:
        return json.load(f)