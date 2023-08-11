import argparse

from src.data.fpl_data_parser import get_season, get_players
from src.model.squad import Squad
from src.model.season import Season
from src.service.difficulty_service import DifficultyService


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--service")
    return parser


def draft_cli_service(season: Season):
    print("------------- Draft CLI ---------------")
    print("1. New Draft")
    print("2. Load Draft")
    print("3. Save Draft")
    print("4. Exit")
    print("----------------------------------------")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("New Draft")
        draft = Squad()
        draft_picker_cli(draft, season)
    elif choice == 2:
        print("Load Draft")
    elif choice == 3:
        print("Save Draft")
    elif choice == 4:
        print("Exiting...")
        exit(0)


def draft_picker_cli(draft: Squad, season: Season):
    while True:
        print("------------- Draft Picker ---------------")
        print("1. Pick Player")
        print("2. View Team")
        print("3. View Draft")
        print("4. Exit")
        print("------------------------------------------")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            print("Pick Player")
            player_id = int(input("Enter Player ID: "))
            player = season.get_player(player_id)
            draft.add_player(player)
        elif choice == 2:
            print("View Team")
        elif choice == 3:
            print("View Draft")
        elif choice == 4:
            print("Exiting...")
            exit(0)


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
        draft_cli_service(season)


