import json
import os
import requests

from datetime import date

FPL_BASE_API_URL = 'https://fantasy.premierleague.com/api/'
FPL_RAW_DATA_ENDPOINT = f'{FPL_BASE_API_URL}/bootstrap-static/'
FPL_FIXTURES_ENDPOINT = f'{FPL_BASE_API_URL}/fixtures/'

PATH = os.path.dirname(__file__)
DOWNLOAD_PATH = os.path.join(PATH, "__CACHE__")
RAW_FILE_NAME = 'fpl_data.json'
FIXTURE_FILE_NAME = 'fpl_fixtures.json'


def download_raw(raw_file_name) -> None:
    response = requests.get(
        url=FPL_RAW_DATA_ENDPOINT,
        params=None
    )
    with open(raw_file_name, 'w') as outfile:
        outfile.write(response.text)


def download_fixtures(fixtures_file_name, gameweek=0) -> None:
    params = None
    if gameweek > 0:
        params = {'event': gameweek}
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=params
    )
    with open(fixtures_file_name, 'w') as outfile:
        outfile.write(response.text)


def get_raw() -> dict:
    download_folder_path = build_download_folder()
    raw_file_path = os.path.join(download_folder_path, RAW_FILE_NAME)
    download_raw(raw_file_path)
    with open(raw_file_path, 'r') as infile:
        return json.loads(infile.read())


def get_fixtures(gameweek=0) -> list[dict]:
    download_folder_path = build_download_folder()
    fixtures_file_path = os.path.join(download_folder_path, FIXTURE_FILE_NAME)
    download_fixtures(fixtures_file_path, gameweek)
    with open(fixtures_file_path, 'r') as infile:
        return json.loads(infile.read())


def build_download_folder():
    today = date.today()
    download_folder = os.path.join(DOWNLOAD_PATH, str(today.year), str(today.month), str(today.day))
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    return download_folder
