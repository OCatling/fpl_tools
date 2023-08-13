from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router

from src.data.fpl_data_parser import get_season

tracer = Tracer()
logger = Logger()
router = Router()


@router.get("/")
@tracer.capture_method
def get_team():
    season = get_season()
    return season.teams


@router.get("/<team_id>")
@tracer.capture_method
def get_team(team_id: str):
    if not team_id.isnumeric():
        raise TypeError("team_id must be an int")
    team_id = int(team_id)
    logger.info(f"team_id= {team_id}")
    season = get_season()
    return season.get_team(team_id)
