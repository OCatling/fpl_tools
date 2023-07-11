from functools import reduce

from src.model.fixture import Fixture
from src.model.season import Season
from src.model.team import Team


class DifficultyService:
    def __init__(self, season: Season, teams_to_exclude: list[Team] = None):
        self._season = season
        if not teams_to_exclude:
            teams_to_exclude = []
        self._teams_to_exclude = teams_to_exclude

    @property
    def season(self) -> Season:
        return self._season

    @season.setter
    def season(self, season: Season) -> None:
        self._season = season

    @staticmethod
    def get_difficulty_from_home_fixtures(fixtures: list[Fixture]) -> int:
        return reduce(lambda x, y: x + y.home_team_difficulty, fixtures, 0)

    @staticmethod
    def get_difficulty_from_away_fixtures(fixtures: list[Fixture]) -> int:
        return reduce(lambda x, y: x + y.away_team_difficulty, fixtures, 0)

    def get_team_difficulty_for_home_games(self, team_id: int, starting_week: int = 0, finish_week: int = 38) -> int:
        fixtures = self.season.organise_fixtures_by_team(starting_week, finish_week)
        team_home_fixtures: list[Fixture] = fixtures[team_id]["home_games"]
        return self.get_difficulty_from_home_fixtures(team_home_fixtures)

    def get_team_difficulty_for_away_games(self, team_id: int, starting_week: int = 0, finish_week: int = 38) -> int:
        fixtures = self.season.organise_fixtures_by_team(starting_week, finish_week)
        team_away_fixtures: list[Fixture] = fixtures[team_id]["away_games"]
        return self.get_difficulty_from_away_fixtures(team_away_fixtures)

    def get_teams_period_difficulty(self, team_id: int, starting_week: int = 0, finish_week: int = 38) -> int:
        return self.get_team_difficulty_for_home_games(team_id, starting_week, finish_week) + \
            self.get_team_difficulty_for_away_games(team_id, starting_week, finish_week)

    def get_all_teams_period_difficulty(self, starting_week: int = 0, finish_week: int = 38):
        fixtures_organised_by_team = self.season.organise_fixtures_by_team(starting_week, finish_week)
        for team_id, team_data in fixtures_organised_by_team.items():
            home_difficulty = self.get_difficulty_from_home_fixtures(team_data["home_games"])
            away_difficulty = self.get_difficulty_from_away_fixtures(team_data["away_games"])

            fixtures_organised_by_team[team_id]["home_difficulty"] = home_difficulty
            fixtures_organised_by_team[team_id]["away_difficulty"] = away_difficulty
            fixtures_organised_by_team[team_id]["difficulty"] = home_difficulty + away_difficulty

        return fixtures_organised_by_team

    def get_list_of_teams_sorted_by_period_difficulty(self, starting_week: int = 0, finish_week: int = 38):
        fixtures_organised_by_team = self.get_all_teams_period_difficulty(starting_week, finish_week)
        return sorted(fixtures_organised_by_team.values(), key=lambda x: x["difficulty"], reverse=True)

