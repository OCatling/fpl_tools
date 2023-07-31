import argparse

from src.data.fpl_data_parser import get_season, get_players
from src.service.difficulty_service_2 import DifficultyService


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--service")
    return parser


if __name__ == "__main__":
    print("------------- FPL CLI ---------------")
    args = get_parser().parse_args()
    if args.service == "fixture":
        start_week = int(input("Enter Start Week: "))
        end_week = int(input("Enter End Week: "))
        season = get_season()
        service = DifficultyService(season)

        teams = service.get_list_of_teams_sorted_by_period_difficulty(start_week, end_week)
        for team in teams:
            print(f"{team['team_name']}: {team['difficulty']}")
            for fixture in team["all_games"]:
                print(f"{fixture.home_team.name}[{fixture.home_team_difficulty}] v {fixture.away_team.name}[{fixture.away_team_difficulty}]")
            print("-------------------------------")
    elif args.service == "player":
        players = get_players()
        print(players)

    elif args.service == "draft":
        season = get_season()


