from src.data import fpl_data_fetcher


def test_get_raw():
    mock_raw_file_location = "test/resources/example_raw_data.json"
    raw_data = fpl_data_fetcher.get_raw(mock_raw_file_location)
    assert raw_data


def test_get_fixtures():
    mock_fixtures_file_location = "test/resources/example_fixtures.json"
    fixtures = fpl_data_fetcher.get_fixtures(mock_fixtures_file_location)
    assert fixtures

# TODO: test download functions
