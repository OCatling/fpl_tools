import uuid

from src.data.model.fantasy_player import FantasyPlayer


class Squad(dict):
    _squad_id: str
    _goalkeepers: list
    _defenders: list
    _midfielders: list
    _forwards: list

    def __init__(self, squad_id: str = None, players: list[FantasyPlayer] = None, *args, **kwargs) -> None:
        self.squad_id = squad_id or str(uuid.uuid4())

        if not players:
            players = []

        goalkeepers = kwargs.get("goalkeepers") or [player for player in players if player.position == "GKP"]
        defenders = kwargs.get("defenders") or [player for player in players if player.position == "DEF"]
        midfielders = kwargs.get("midfielders") or [player for player in players if player.position == "MID"]
        forwards = kwargs.get("forwards") or [player for player in players if player.position == "FWD"]

        self.goalkeepers = goalkeepers
        self.defenders = defenders
        self.midfielders = midfielders
        self.forwards = forwards
        dict.__init__(self, goalkeepers=goalkeepers, defenders=defenders, midfielders=midfielders, forwards=forwards)

    @property
    def squad_id(self) -> str:
        return self._squad_id

    @squad_id.setter
    def squad_id(self, squad_id: str) -> None:
        if not isinstance(squad_id, str):
            raise TypeError("squad_id must be a string")
        self._squad_id = squad_id

    @property
    def goalkeepers(self) -> list:
        return self._goalkeepers

    @goalkeepers.setter
    def goalkeepers(self, goalkeepers: list) -> None:
        if not isinstance(goalkeepers, list):
            raise TypeError("goalkeepers must be a list")
        if len(goalkeepers) > 2:
            raise ValueError("goalkeepers must be a list of 2 goalkeepers")
        self._goalkeepers = goalkeepers

    @property
    def defenders(self) -> list:
        return self._defenders

    @defenders.setter
    def defenders(self, defenders: list) -> None:
        if not isinstance(defenders, list):
            raise TypeError("defenders must be a list")
        if len(defenders) > 5:
            raise ValueError("defenders must be a list of 5 defenders")
        self._defenders = defenders

    @property
    def midfielders(self) -> list:
        return self._midfielders

    @midfielders.setter
    def midfielders(self, midfielders: list) -> None:
        if not isinstance(midfielders, list):
            raise TypeError("midfielders must be a list")
        if len(midfielders) > 5:
            raise ValueError("midfielders must be a list of 5 midfielders")
        self._midfielders = midfielders

    @property
    def forwards(self) -> list:
        return self._forwards

    @forwards.setter
    def forwards(self, forwards: list) -> None:
        if not isinstance(forwards, list):
            raise TypeError("forwards must be a list")
        if len(forwards) > 3:
            raise ValueError("forwards must be a list of 3 forwards")
        self._forwards = forwards

    def get_players(self) -> list[FantasyPlayer]:
        return self.goalkeepers + self.defenders + self.midfielders + self.forwards

    def get_players_ids(self) -> list[str]:
        return [player.id for player in self.get_players()]

    def add_goalkeeper(self, goalkeeper: FantasyPlayer) -> None:
        if len(self.goalkeepers) == 2:
            raise ValueError("You cannot have more than 2 goalkeepers")
        self.goalkeepers.append(goalkeeper)

    def add_defender(self, defender: FantasyPlayer) -> None:
        if len(self.defenders) == 5:
            raise ValueError("You cannot have more than 5 defenders")
        self.defenders.append(defender)

    def add_midfielder(self, midfielder: FantasyPlayer) -> None:
        if len(self.midfielders) == 5:
            raise ValueError("You cannot have more than 5 midfielders")
        self.midfielders.append(midfielder)

    def add_forward(self, forward: FantasyPlayer) -> None:
        if len(self.forwards) == 3:
            raise ValueError("You cannot have more than 3 forwards")
        self.forwards.append(forward)

    def remove_goalkeeper(self, goalkeeper: FantasyPlayer) -> None:
        self.goalkeepers.remove(goalkeeper)

    def remove_defender(self, defender: FantasyPlayer) -> None:
        self.defenders.remove(defender)

    def remove_midfielder(self, midfielder: FantasyPlayer) -> None:
        self.midfielders.remove(midfielder)

    def remove_forward(self, forward: FantasyPlayer) -> None:
        self.forwards.remove(forward)

    def add_player(self, player: FantasyPlayer) -> None:
        if player.position == 1:
            self.add_goalkeeper(player)
        elif player.position == 2:
            self.add_defender(player)
        elif player.position == 3:
            self.add_midfielder(player)
        elif player.position == 4:
            self.add_forward(player)
        else:
            raise ValueError("Invalid position")

    def remove_player(self, player: FantasyPlayer) -> None:
        if player.position == 1:
            self.remove_goalkeeper(player)
        elif player.position == 2:
            self.remove_defender(player)
        elif player.position == 3:
            self.remove_midfielder(player)
        elif player.position == 4:
            self.remove_forward(player)
        else:
            raise ValueError("Invalid position")

    def get_total_cost(self) -> int:
        return sum([player.now_cost for player in self.get_players()])

    def get_total_points(self) -> int:
        return sum([player.total_points for player in self.get_players()])

    def __str__(self) -> str:
        return f"Squad(squad_id={self.squad_id}," \
               f"goalkeepers={self.goalkeepers}, " \
               f"defenders={self.defenders}, " \
               f"midfielders={self.midfielders}, " \
               f"forwards={self.forwards})"
