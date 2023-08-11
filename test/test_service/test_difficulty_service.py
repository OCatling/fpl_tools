# from unittest.mock import patch
#
# import pytest
#
# from src.service.difficulty_service import DifficultyService
#
#
# def test_calculate_period_difficulty_for_team_home_fixtures():
#     with patch('src.service.fixture_service.get_team_home_fixtures') as mock_home_fixtures:
#         mock_home_fixtures.return_value = [
#             {'team_h_difficulty': 5},
#             {'team_h_difficulty': 2},
#             {'team_h_difficulty': 3}
#         ]
#         service = DifficultyService()
#         actual = difficulty_service.get_team_difficulty_for_home_games(1, 1, 38)
#         assert actual == 10
#
#
# def test_calculate_period_difficulty_for_team_away_fixtures():
#     with patch('src.service.fixture_service.get_team_away_fixtures') as mock_away_fixtures:
#         mock_away_fixtures.return_value = [
#             {'team_a_difficulty': 4},
#             {'team_a_difficulty': 2},
#             {'team_a_difficulty': 1}
#         ]
#         actual = difficulty_service.get_period_difficulty_for_team_away_games(1, 1, 38)
#         assert actual == 7
#
#
# def test_calculate_period_difficulty_for_team():
#     with patch('src.service.fixture_service.get_team_away_fixtures') as mock_away_fixtures:
#         mock_away_fixtures.return_value = [
#             {'team_a_difficulty': 5},
#             {'team_a_difficulty': 5},
#             {'team_a_difficulty': 1}
#         ]
#         with patch('src.service.fixture_service.get_team_home_fixtures') as mock_home_fixtures:
#             mock_home_fixtures.return_value = [
#                 {'team_h_difficulty': 2},
#                 {'team_h_difficulty': 2},
#                 {'team_h_difficulty': 3}
#             ]
#             actual = difficulty_service.get_period_difficulty_for_team(1, 1, 38)
#             assert actual == 18
