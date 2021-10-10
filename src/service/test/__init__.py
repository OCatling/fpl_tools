import json


def get_example_raw():
    with open('./src/service/test/resources/fpl_data.json', 'r') as infile:
        return json.loads(infile.read())
