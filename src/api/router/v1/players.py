from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router

from src.data.fpl_data_parser import get_season

tracer = Tracer()
logger = Logger()
router = Router()


@router.get("/")
@tracer.capture_method
def get_players():
    season = get_season()
    logger.info({"players": season.players})
    return {"players": season.players}


@router.get("/<player_id>")
@tracer.capture_method
def get_player(player_id: str):
    if not player_id.isnumeric():
        raise TypeError("player_id must be an int")
    player_id = int(player_id)
    logger.info(f"player_id= {player_id}")
    season = get_season()
    return season.get_player(player_id)
