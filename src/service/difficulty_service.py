from collections import Counter
from functools import reduce

from src.service import fixture_service, team_service


def get_period_difficulty_for_team_home_games(team_id: int, start_week: int, end_week: int) -> int:
    fixtures = fixture_service.get_team_home_fixtures(team_id, start_week, end_week)
    return reduce(lambda x, y: x + y['team_h_difficulty'], fixtures, 0)


def get_period_difficulty_for_team_away_games(team_id: int, start_week: int, end_week: int) -> int:
    fixtures = fixture_service.get_team_away_fixtures(team_id, start_week, end_week)
    return reduce(lambda x, y: x + y['team_a_difficulty'], fixtures, 0)


def get_period_difficulty_for_team(team_id: int, start_week: int, end_week: int) -> int:
    return get_period_difficulty_for_team_home_games(team_id, start_week, end_week) + \
           get_period_difficulty_for_team_away_games(team_id, start_week, end_week)


def get_teams_with_easy_home_fixtures(start_week: int, end_week: int) -> list[dict]:
    teams_with_easy_fixtures = [
        team_service.get_team(fixture['team_h']) for fixture
        in fixture_service.get_fixtures(start_week, end_week)
        if fixture['team_h_difficulty'] < 3
    ]
    return [
        dict(team) for team
        in {tuple(d.items()) for d in teams_with_easy_fixtures}
    ]


def get_teams_with_easy_away_fixtures(start_week: int, end_week: int) -> list[dict]:
    teams_with_easy_fixtures = [
        team_service.get_team(fixture['team_a']) for fixture
        in fixture_service.get_fixtures(start_week, end_week)
        if fixture['team_a_difficulty'] < 3
    ]
    return [
        dict(team) for team
        in {tuple(d.items()) for d in teams_with_easy_fixtures}
    ]


def get_teams_with_easy_fixtures(start_week: int, end_week: int):
    teams_with_easy_fixtures = \
        get_teams_with_easy_home_fixtures(start_week, end_week) + \
        get_teams_with_easy_away_fixtures(start_week, end_week)
    return [
        dict(team) for team
        in {tuple(d.items()) for d in teams_with_easy_fixtures}
    ]


def get_rotation_teams_for_home_fixtures(team_id: int, start_week: int, end_week: int) -> Counter:
    fixtures = fixture_service.get_team_home_fixtures(team_id, start_week, end_week)
    rotating_teams = Counter()
    for fixture in fixtures:
        if fixture['team_h_difficulty'] >= 4:
            gameweek = fixture['event']
            for f in get_teams_with_easy_fixtures(gameweek, gameweek):
                teams = []
                if f['team_h_difficulty'] <= 2:
                    teams.append(team_service.get_team(f['team_h'])['name'])
                if f['team_a_difficulty'] <= 2:
                    teams.append(team_service.get_team(f['team_a'])['name'])
                rotating_teams.update(teams)
    return rotating_teams
