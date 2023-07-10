from src.model.season import Season
from src.model.team import Team

mock_teams = [Team({})]


class TestSeason:
    def test_construction(self):
        Season("test_season", )