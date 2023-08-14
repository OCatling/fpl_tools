from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router

from src.data.fpl_data_parser import get_season
from src.model.squad import Squad

tracer = Tracer()
logger = Logger()
router = Router()


@router.post("/")
def create_squad():
    pass


@router.put("/<squad_id>")
def update_squad(squad_id: str, ):
    pass


@router.get("/<squad_id>")
def get_squad(squad_id: str):
    pass


@router.get("/")
def get_squads():
    pass


@router.delete("/<squad_id>")
def delete_squad(squad_id: str):
    pass
