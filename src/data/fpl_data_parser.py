from src.data import fpl_data_fetcher
from src.model.fixture import Fixture
from src.model.season import Season
from src.model.team import Team


def get_teams() -> dict[int: Team]:
    teams = fpl_data_fetcher.get_raw()['teams']
    team_objs = [Team(i) for i in teams]
    return {team.id: team for team in team_objs}


def get_fixtures() -> dict[int: list[Fixture]]:
    fixtures = fpl_data_fetcher.get_fixtures()
    teams = get_teams()
    fixture_objs = {}
    for fixture in fixtures:
        home_team_id = fixture["team_h"]
        home_team = teams[home_team_id]
        away_team_id = fixture["team_a"]
        away_team = teams[away_team_id]

        gameweek = fixture["event"]
        if gameweek not in fixture_objs.keys():
            fixture_objs[gameweek] = []

        fixture_obj = Fixture(home_team, away_team, fixture)
        fixture_objs[gameweek].append(fixture_obj)

    return fixture_objs


def get_league():
    teams = get_teams()
    fixtures = get_fixtures()
    # TODO: unhardcode season
    return Season("2023/2024", teams, fixtures)