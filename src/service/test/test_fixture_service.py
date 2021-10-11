from unittest.mock import patch

import pytest

from src.service import fixture_service
from src.service.test import get_example_fixtures


def test_get_fixtures():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_fixtures(1, 2)

        assert isinstance(actual, list)
        assert len(actual) == 20


def test_get_team_fixtures_team_exists():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_fixtures(1, 1, 38)

        assert isinstance(actual, list)
        assert len(actual) == 38


def test_get_team_fixtures_team_nonexistent():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_fixtures(0, 1, 38)

        assert isinstance(actual, list)
        assert len(actual) == 0


def test_get_team_home_fixtures_team_exists():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_home_fixtures(1, 1, 38)

        assert isinstance(actual, list)
        assert len(actual) == 19


def test_get_team_home_fixtures_team_nonexistent():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_home_fixtures(0, 1, 38)

        assert isinstance(actual, list)
        assert len(actual) == 0


def test_get_team_away_fixtures_team_exists():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_away_fixtures(1, 1, 20)

        assert isinstance(actual, list)
        assert len(actual) == 10


def test_get_team_away_fixtures_team_nonexistent():
    with patch('src.data.get_fixtures') as mock_get_fixtures:
        mock_get_fixtures.return_value = get_example_fixtures()
        actual = fixture_service.get_team_away_fixtures(0, 1, 20)

        assert isinstance(actual, list)
        assert len(actual) == 0
