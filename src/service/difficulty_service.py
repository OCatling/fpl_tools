from functools import reduce

from src.service import fixture_service


def get_period_difficulty_for_team_home_games(team_id: int, start_week: int, end_week: int) -> int:
    fixtures = fixture_service.get_team_home_fixtures(team_id, start_week, end_week)
    return reduce(lambda x, y: x + y['team_h_difficulty'], fixtures, 0)


def get_period_difficulty_for_team_away_games(team_id: int, start_week: int, end_week: int) -> int:
    fixtures = fixture_service.get_team_away_fixtures(team_id, start_week, end_week)
    return reduce(lambda x, y: x + y['team_a_difficulty'], fixtures, 0)


def get_period_difficulty_for_team(team_id: int, start_week: int, end_week: int) -> int:
    return get_period_difficulty_for_team_home_games(team_id, start_week, end_week) + \
           get_period_difficulty_for_team_away_games(team_id, start_week, end_week)
