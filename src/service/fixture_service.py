from src import data


def get_team_fixtures(team_id: int, start_week: int, end_week: int) -> list[dict]:
    fixtures = data.get_fixtures()
    return [
            f for f in fixtures if
            (start_week <= f['event'] <= end_week) and
            (f['team_h'] == team_id or f['team_a'] == team_id)
        ]


def get_team_home_fixtures(team_id: int, start_week: int, end_week: int) -> list[dict]:
    fixtures = data.get_fixtures()
    return [
            f for f in fixtures if
            (start_week <= f['event'] <= end_week) and
            (f['team_h'] == team_id)
        ]


def get_team_away_fixtures(team_id: int, start_week: int, end_week: int) -> list[dict]:
    fixtures = data.get_fixtures()
    return [
            f for f in fixtures if
            (start_week <= f['event'] <= end_week) and
            (f['team_a'] == team_id)
        ]
