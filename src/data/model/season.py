from __future__ import annotations

from src.data.model.fantasy_player import FantasyPlayer
from src.data.model.fixture import Fixture
from src.data.model.team import Team


class Season:
    _players: list[FantasyPlayer] = None

    def __init__(self, season: str, teams: dict, fixtures: list[Fixture], players: list[FantasyPlayer]) -> None:
        self._season = season
        self._teams = teams
        self._fixtures = fixtures
        self.players = players

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

    @property
    def players(self) -> list[FantasyPlayer]:
        return self._players

    @players.setter
    def players(self, players: list[FantasyPlayer]) -> None:
        if not isinstance(players, list):
            raise TypeError("players must be a list of FantasyPlayer objects")
        self._players = players

    def get_team(self, _id: int) -> Team:
        return self._teams[_id]

    def get_team_by_name(self, name: str) -> Team:
        teams = self.get_teams_by_name()
        return teams[name]

    def add_team(self, team: Team) -> None:
        self._teams[team.id] = team

    def delete_team(self, team: Team) -> None:
        del self._teams[team.id]

    def add_fixture(self, fixture: Fixture) -> None:
        self._fixtures.append(fixture)

    def delete_fixture(self, fixture):
        self._fixtures.remove(fixture)

    def get_player(self, _id: int) -> FantasyPlayer:
        player = [player for player in self._players if player.id == _id]
        if len(player) == 0:
            raise ValueError(f"Player with id {_id} not found")
        return player[0]

    def add_player(self, player: FantasyPlayer) -> None:
        self._players.append(player)

    def delete_player(self, player: FantasyPlayer) -> None:
        self._players.remove(player)

    def get_players_by_team(self, team: Team) -> list[FantasyPlayer]:
        return [player for player in self._players if player.team == team]

    def get_players_by_position(self, position: str) -> list[FantasyPlayer]:
        return [player for player in self._players if player.position == position]

    def get_players_by_team_and_position(self, team: Team, position: str) -> list[FantasyPlayer]:
        return [player for player in self._players if player.team == team and player.position == position]

    def get_players_organised_by_team(self) -> dict[int: list[FantasyPlayer]]:
        players_by_team = {}
        for player in self.players:
            if player.team_id not in players_by_team.keys():
                players_by_team[player.team_id] = []
            players_by_team[player.team_id].append(player)
        return players_by_team

    def get_players_organised_by_position(self) -> dict[str: list[FantasyPlayer]]:
        players_by_position = {}
        for player in self.players:
            if player.position not in players_by_position.keys():
                players_by_position[player.position] = []
            players_by_position[player.position].append(player)
        return players_by_position

    def get_organize_players_by_team_and_position(self) -> dict[int: dict[str: list[FantasyPlayer]]]:
        players_by_team_and_position = {}
        for player in self.players:
            if player.team_id not in players_by_team_and_position.keys():
                players_by_team_and_position[player.team_id] = {}
            if player.position not in players_by_team_and_position[player.team_id].keys():
                players_by_team_and_position[player.team_id][player.position] = []
            players_by_team_and_position[player.team_id][player.position].append(player)
        return players_by_team_and_position

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

    def get_teams_by_name(self) -> dict[str: Team]:
        return {team.name: team for team in self.teams.values()}
