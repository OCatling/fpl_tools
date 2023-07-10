from src.data.fpl_data_parser import get_season


if __name__ == "__main__":
    print("------------- FPL CLI ---------------")
    start_week = input("Enter Start Week: ")
    end_week = input("Enter End Week: ")
    season = get_season()

    games = season.organise_fixtures_by_team(0, 3)
    for key in games.keys():
        print(f"{key}: {[f.away_team for f in games[key]['home']]}")
