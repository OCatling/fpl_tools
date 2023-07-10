from src.service.difficulty_service import get_teams_with_easy_fixtures
from src.model.team import Team

if __name__ == "__main__":
    print("------------- FPL CLI ---------------")
    start_week = input("Enter Start Week: ")
    end_week = input("Enter End Week: ")
    teams = get_teams_with_easy_fixtures(0, 5)
    for team in teams:
        t = Team(team)
        print(f"{t.id}: {t.name}")
        print("=========================")
