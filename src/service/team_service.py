from src import data


def get_teams() -> list:
    return data.get_raw()['teams']


def get_team_from_name(team_name: str) -> dict:
    return next((team for team in get_teams() if team['name'].lower() == team_name.lower()), None)


def get_team(team_id: int) -> dict:
    return next((team for team in get_teams() if team['id'] == team_id), None)
