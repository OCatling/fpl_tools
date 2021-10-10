import json
import os
import requests

FPL_BASE_API_URL = 'https://fantasy.premierleague.com/api/'
FPL_DATA_ENDPOINT = f'{FPL_BASE_API_URL}/bootstrap-static/'
FPL_FIXTURES_ENDPOINT = f'{FPL_BASE_API_URL}/fixtures/'

DATA_FILE = 'fpl_data.json'
FIXTURE_FILE = 'fpl_fixtures.json'


def download_data() -> None:
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=None
    )
    with open(f'./{DATA_FILE}', 'w') as outfile:
        outfile.write(response.text)


def download_fixtures(gameweek=0) -> None:
    params = None
    if gameweek > 0:
        params = {'event': gameweek}
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=params
    )
    with open(f'./{FIXTURE_FILE}', 'w') as outfile:
        outfile.write(response.text)


def get_data() -> list:
    if not os.path.exists(DATA_FILE):
        download_data()
    with open(DATA_FILE, 'r') as infile:
        return json.loads(infile.read())


def get_fixtures(gameweek=0) -> list:
    if not os.path.exists(FIXTURE_FILE):
        download_fixtures(gameweek)
    with open(FIXTURE_FILE, 'r') as infile:
        return json.loads(infile.read())


get_fixtures()
get_data()
