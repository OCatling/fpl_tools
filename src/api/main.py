from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from src.api.router.v1 import teams, players, difficulty

tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()

app.include_router(players.router, prefix="/players")
app.include_router(teams.router, prefix="/teams")
app.include_router(difficulty.router, prefix="/difficulty")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
