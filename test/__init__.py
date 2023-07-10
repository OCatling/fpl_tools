import json


def get_example_raw() -> dict:
    with open('./test/resources/example_raw_data.json', 'r') as infile:
        return json.loads(infile.read())


def get_example_fixtures() -> list[dict]:
    with open('./test/resources/example_fixtures.json', 'r') as infile:
        return json.loads(infile.read())
