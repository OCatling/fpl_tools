from datetime import datetime

from src.model.team import Team


class Fixture:
    def __init__(self, home_team: Team, away_team: Team, fixture: dict) -> None:
        self._fixture = fixture

        self._code = self._fixture["code"]
        self._event = self._fixture["event"]
        self._fixture_id = self._fixture["id"]

        self._kickoff_time = datetime.strptime(self._fixture["kickoff_time"], '%Y-%m-%dT%H:%M:%Sz')

        self._home_team = home_team
        self._home_team_difficulty = self._fixture["team_h_difficulty"]
        self._home_team_goals = self._fixture["team_h_score"]

        self._away_team = away_team
        self._away_team_difficulty = self._fixture["team_a_difficulty"]
        self._away_team_goals = self._fixture["team_a_score"]

    # ===== INFO =====
    @property
    def fixture(self) -> dict:
        return self._fixture

    @fixture.setter
    def fixture(self, fixture: dict) -> None:
        self._fixture = fixture

    @property
    def kickoff_time(self) -> datetime:
        return self._kickoff_time

    @kickoff_time.setter
    def kickoff_time(self, kickoff_time: str) -> None:
        self._kickoff_time = datetime.fromisoformat(kickoff_time)

    def fixture_has_kicked_off(self) -> bool:
        return self._kickoff_time > datetime.now()

    @property
    def event(self) -> int:
        return self._event

    @event.setter
    def event(self, event: int) -> None:
        self._event = event

    @property
    def id(self) -> int:
        return self._fixture_id

    @id.setter
    def id(self, fixture_id) -> None:
        self._fixture_id = fixture_id

    # ===== HOME =====
    @property
    def home_team(self) -> Team:
        return self._home_team

    @home_team.setter
    def home_team(self, home_team: Team) -> None:
        self._home_team = home_team

    @property
    def home_team_difficulty(self) -> int:
        return self._home_team_difficulty

    @home_team_difficulty.setter
    def home_team_difficulty(self, home_team_difficulty: int) -> None:
        self._home_team_difficulty = home_team_difficulty

    # ===== AWAY =====
    @property
    def away_team(self) -> Team:
        return self._away_team

    @away_team.setter
    def away_team(self, away_team: Team) -> None:
        self._away_team = away_team

    @property
    def away_team_difficulty(self) -> int:
        return self._away_team_difficulty

    @away_team_difficulty.setter
    def away_team_difficulty(self, away_team_difficulty: int) -> None:
        self._away_team_difficulty = away_team_difficulty

