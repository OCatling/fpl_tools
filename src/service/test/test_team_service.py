import pytest

from unittest.mock import patch

from src.service import team_service
from src.service.test import get_example_raw


def test_get_teams():
    with patch('src.data.get_raw') as mock_raw:
        mock_raw.return_value = get_example_raw()
        actual = team_service.get_teams()

        assert isinstance(actual, list)
        assert len(actual) is 20


def test_get_team_from_name_exists():
    with patch('src.data.get_raw') as mock_raw:
        mock_raw.return_value = get_example_raw()
        actual = team_service.get_team_from_name('ARSENAL')

        assert isinstance(actual, dict)
        assert 'name' in actual
        assert 'id' in actual
        assert actual['name'] == 'Arsenal'
        assert actual['id'] == 1


def test_get_team_from_name_does_not_exist():
    with patch('src.data.get_raw') as mock_raw:
        mock_raw.return_value = get_example_raw()
        actual = team_service.get_team_from_name('THIS TEAM NAME DOES NOT EXIST')

        assert actual is None


def test_get_team_exists():
    with patch('src.data.get_raw') as mock_raw:
        mock_raw.return_value = get_example_raw()
        actual = team_service.get_team(1)

        assert isinstance(actual, dict)
        assert 'name' in actual
        assert 'id' in actual
        assert actual['name'] == 'Arsenal'
        assert actual['id'] == 1


def test_get_team_does_not_exist():
    with patch('src.data.get_raw') as mock_raw:
        mock_raw.return_value = get_example_raw()
        actual = team_service.get_team(0)

        assert actual is None
