import json
import os
import requests

FPL_BASE_API_URL = 'https://fantasy.premierleague.com/api/'
FPL_RAW_DATA_ENDPOINT = f'{FPL_BASE_API_URL}/bootstrap-static/'
FPL_FIXTURES_ENDPOINT = f'{FPL_BASE_API_URL}/fixtures/'

PATH = os.path.dirname(__file__)
DOWNLOAD_PATH = os.path.join(PATH, "__CACHE__")
RAW_FILE_NAME = os.path.join(DOWNLOAD_PATH, 'fpl_data.json')
FIXTURE_FILE_NAME = os.path.join(DOWNLOAD_PATH, 'fpl_fixtures.json')


def download_raw(raw_file_name="") -> None:
    if not raw_file_name:
        raw_file_name = RAW_FILE_NAME
    response = requests.get(
        url=FPL_RAW_DATA_ENDPOINT,
        params=None
    )
    with open(raw_file_name, 'w') as outfile:
        outfile.write(response.text)


def download_fixtures(fixtures_file_name="", gameweek=0) -> None:
    if not fixtures_file_name:
        fixtures_file_name = FIXTURE_FILE_NAME
    params = None
    if gameweek > 0:
        params = {'event': gameweek}
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=params
    )
    with open(fixtures_file_name, 'w') as outfile:
        outfile.write(response.text)


def get_raw(raw_file_name="") -> dict:
    if not raw_file_name:
        raw_file_name = RAW_FILE_NAME
    if not os.path.exists(raw_file_name):
        download_raw()
    with open(raw_file_name, 'r') as infile:
        return json.loads(infile.read())


def get_fixtures(fixtures_file_name="", gameweek=0) -> list[dict]:
    if not fixtures_file_name:
        fixtures_file_name = FIXTURE_FILE_NAME
    if not os.path.exists(fixtures_file_name):
        download_fixtures(fixtures_file_name, gameweek)
    with open(fixtures_file_name, 'r') as infile:
        return json.loads(infile.read())
