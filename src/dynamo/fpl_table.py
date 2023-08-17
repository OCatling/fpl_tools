import os

from boto3 import resource
from boto3.dynamodb.conditions import Key

from src.model.season import Season
from src.model.squad import Squad


class FPLTable:
    def __init__(self, name: str, season: Season) -> None:
        self.name = name

        if os.getenv("AWS_SAM_LOCAL"):
            self.table = resource('dynamodb', endpoint_url="http://docker.for.mac.localhost:8000/").Table(name)
        else:
            self.table = resource('dynamodb').Table(name)
        self.season = season

    def get_squads(self, user_id: str, squad_id: str = None, *args, **kwargs) -> list[Squad]:
        primary_key = f"SQUAD#{user_id}"
        expression = Key("<primary_key>").eq(primary_key)

        if squad_id:
            expression = expression & Key("<partition_key>").begins_with(squad_id)

        response = self.table.query(
            KeyConditionExpression=expression,
            ScanIndexForward=False,
            **kwargs
        )
        items = response.get('Items', [])

        squads = []
        for squad_data in items:
            players = [self.season.get_player(player_id) for player_id in squad_data.get('player_ids', [])]
            squad_id = squad_data.get('<partition_key>')
            squads.append(Squad(squad_id, players))
        return squads

    def get_squad(self, user_id: str, squad_id: str) -> Squad:
        squads = self.get_squads(user_id, squad_id, Limit=1)
        if len(squads) > 0:
            return squads[0]

    def put_squad(self, user_id: str, squad: Squad) -> dict:
        primary_key = f"SQUAD#{user_id}"
        return self.table.put_item(Item={
            "<primary_key>": primary_key,
            "<partition_key>": squad.squad_id,
            "player_ids": squad.get_players_ids()
        })

    def delete_squad(self, user_id: str, squad_id: str) -> dict:
        # TODO: implement
        pass

    def update_squad(self, user_id: str, squad_id: str, squad: Squad) -> dict:
        # TODO: implement
        pass
