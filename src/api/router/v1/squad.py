from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router

from src.data.fpl_data_parser import get_season
from src.dynamo.fpl_table import FPLTable
from src.model.squad import Squad

tracer = Tracer()
logger = Logger()
router = Router()


@router.post("/<user_id>")
def create_squad(user_id: str):
    # TODO: get from env
    table_name = "FPL"
    season = get_season()
    fpl_table = FPLTable(table_name, season)

    squad = Squad()
    fpl_table.put_squad(user_id, squad)
    return {"id": squad.squad_id}


@router.put("/<user_id>/<squad_id>")
def update_squad(user_id: str, squad_id: str):
    pass


@router.get("/<user_id>/<squad_id>")
def get_squad(user_id: str, squad_id: str):
    # TODO: get from env
    table_name = "FPL"
    season = get_season()
    fpl_table = FPLTable(table_name, season)

    squad = fpl_table.get_squad(user_id, squad_id)
    logger.info(f"squad={squad}")
    return squad


@router.get("/<user_id>")
def get_squads(user_id: str):
    # TODO: get from env
    table_name = "FPL"
    season = get_season()
    fpl_table = FPLTable(table_name, season)

    squads = fpl_table.get_squads(user_id)
    return squads


@router.delete("/<user_id>/<squad_id>")
def delete_squad(user_id: str, squad_id: str):
    pass
