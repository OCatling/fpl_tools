from __future__ import annotations

from src.model.fixture import Fixture
from src.model.team import Team


class Season:
    def __init__(self, season: str, teams: dict, fixtures: list[Fixture]) -> None:
        self._season = season
        self._teams = teams
        self._fixtures = fixtures

    @property
    def teams(self) -> dict[int: Team]:
        return self._teams

    @teams.setter
    def teams(self, teams: dict) -> None:
        self._teams = teams

    @property
    def fixtures(self) -> list[Fixture]:
        return self._fixtures

    @fixtures.setter
    def fixtures(self, fixtures: list[Fixture]) -> None:
        self._fixtures = fixtures

    def get_team(self, _id: int) -> Team:
        return self._teams[_id]

    def get_team_by_name(self, name: str) -> Team:
        teams = {team.name: team for team in self._teams.items()}
        return teams[name]

    def add_team(self, team: Team) -> None:
        self._teams[team.id] = team

    def delete_team(self, team: Team) -> None:
        del self._teams[team.id]

    def add_fixture(self, fixture: Fixture) -> None:
        self._fixtures.append(fixture)

    def delete_fixture(self, fixture):
        self._fixtures.remove(fixture)

    def get_specific_gameweek_range(self, starting_week: int = 0, finish_week: int = 38):
        return [f for f in self.fixtures if starting_week <= f.event <= finish_week]

    def get_teams_fixtures(self, team_id: int, starting_week: int = 0, finish_week: int = 38) -> list[Fixture]:
        fixtures = self.get_specific_gameweek_range(starting_week, finish_week)
        return [f for f in fixtures if f.home_team.id == team_id or f.away_team.id == team_id]

    def organise_fixtures_by_gameweek(self, starting_week: int = 0, finishing_week: int = 38) -> dict[int, list]:
        fixtures = self.get_specific_gameweek_range(starting_week, finishing_week)
        fixtures_by_gameweek = {}
        for fixture in fixtures:
            if fixture.event not in fixtures_by_gameweek.keys():
                fixtures_by_gameweek[fixture.event] = []
            fixtures_by_gameweek[fixture.event].append(fixture)
        return fixtures_by_gameweek

    def organise_fixtures_by_team(self,
                                  starting_week: int = 0,
                                  finishing_week: int = 38
                                  ) -> dict[str: dict[str: list[Fixture]]]:
        fixtures = self.get_specific_gameweek_range(starting_week, finishing_week)
        fixtures_by_team = {team.id: {"team_name": team.name, "home_games": [], "away_games": [], "all_games": []} for team in self.teams.values()}
        for fixture in fixtures:
            fixtures_by_team[fixture.home_team.id]["home_games"].append(fixture)
            fixtures_by_team[fixture.home_team.id]["all_games"].append(fixture)
            fixtures_by_team[fixture.away_team.id]["away_games"].append(fixture)
            fixtures_by_team[fixture.away_team.id]["all_games"].append(fixture)
        return fixtures_by_team
