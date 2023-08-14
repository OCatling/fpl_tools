from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router

from src.data.fpl_data_parser import get_season
from src.service.difficulty_service import DifficultyService

tracer = Tracer()
logger = Logger()
router = Router()


@router.get("/<starting_week>/<ending_week>")
@tracer.capture_method
def get_teams_difficulty(starting_week: str, ending_week: str):
    if not starting_week.isnumeric():
        raise TypeError("starting_week must be an int")
    starting_week = int(starting_week)
    logger.info(f"starting_week= {starting_week}")

    if not ending_week.isnumeric():
        raise TypeError("ending_week must be an int")
    ending_week = int(ending_week)
    logger.info(f"ending_week= {ending_week}")

    season = get_season()
    difficulty_service = DifficultyService(season)
    return difficulty_service.get_all_teams_period_difficulty(starting_week, ending_week)


@router.get("/<team_id>/<starting_week>/<ending_week>")
@tracer.capture_method
def get_team_difficulty(team_id: str, starting_week: str, ending_week: str):
    if not team_id.isnumeric():
        raise TypeError("team_id must be an int")
    team_id = int(team_id)
    logger.info(f"team_id= {team_id}")

    if not starting_week.isnumeric():
        raise TypeError("starting_week must be an int")
    starting_week = int(starting_week)
    logger.info(f"starting_week= {starting_week}")

    if not ending_week.isnumeric():
        raise TypeError("ending_week must be an int")
    ending_week = int(ending_week)
    logger.info(f"ending_week= {ending_week}")

    season = get_season()
    difficulty_service = DifficultyService(season)
    return difficulty_service.get_teams_period_difficulty(team_id, starting_week, ending_week)
