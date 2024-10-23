import asyncio
import time

import requests

from src.aws import s3

FPL_BASE_API_URL = 'https://fantasy.premierleague.com/api/'
FPL_RAW_DATA_ENDPOINT = f'{FPL_BASE_API_URL}/bootstrap-static/'
FPL_FIXTURES_ENDPOINT = f'{FPL_BASE_API_URL}/fixtures/'

RAW_FILE_NAME = 'fpl_data.json'
FIXTURE_FILE_NAME = 'fpl_fixtures.json'

FPL_DATA_BUCKET = 'fpl-data'


def handler(event, context):
    async def main():
        fetch_raw_task = asyncio.create_task(fetch_raw_data())
        fetch_fixtures_task = asyncio.create_task(fetch_fixture_data())
        return await fetch_raw_task, await fetch_fixtures_task
    asyncio.run(main())


async def fetch_raw_data():
    response = requests.get(
        url=FPL_RAW_DATA_ENDPOINT,
        params=None
    )
    s3.Bucket(FPL_DATA_BUCKET).put_object(RAW_FILE_NAME, response.text)
    return response.text


async def fetch_fixture_data():
    response = requests.get(
        url=FPL_FIXTURES_ENDPOINT,
        params=None
    )
    s3.Bucket(FPL_DATA_BUCKET).put_object(FIXTURE_FILE_NAME, response.text)
    return response.text

if __name__ == "__main__":
    handler({},{})
