import json
import os
import requests

FPL_BASE_API_URL = 'https://fantasy.premierleague.com/api/'
FPL_RAW_DATA_ENDPOINT = f'{FPL_BASE_API_URL}/bootstrap-static/'
FPL_FIXTURES_ENDPOINT = f'{FPL_BASE_API_URL}/fixtures/'

PATH = os.path.dirname(__file__)
RAW_FILE_NAME = os.path.join(PATH, 'fpl_data.json')
FIXTURE_FILE_NAME = os.path.join(PATH, 'fpl_fixtures.json')


def download_raw() -> None:
    response = requests.get(
        url=FPL_RAW_DATA_ENDPOINT,
        params=None
    )
    with open(RAW_FILE_NAME, 'w') as outfile:
        outfile.write(response.text)


def download_fixtures(gameweek=0) -> None:
    params = None
    if gameweek > 0:
        params = {'event': gameweek}
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=params
    )
    with open(FIXTURE_FILE_NAME, 'w') as outfile:
        outfile.write(response.text)


def get_raw() -> dict:
    if not os.path.exists(RAW_FILE_NAME):
        download_raw()
    with open(RAW_FILE_NAME, 'r') as infile:
        return json.loads(infile.read())


def get_fixtures(gameweek=0) -> list:
    if not os.path.exists(FIXTURE_FILE_NAME):
        download_fixtures(gameweek)
    with open(FIXTURE_FILE_NAME, 'r') as infile:
        return json.loads(infile.read())
