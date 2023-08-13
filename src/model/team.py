from src.model.player import Player


class Team(dict):
    _players: list[Player] = None

    _id: int = None
    _name: str = None
    _code: int = None
    _strength_overall_home = None
    _strength_overall_away = None
    _strength_attack_home = None
    _strength_attack_away = None
    _strength_defence_home = None
    _strength_defence_away = None
    _wins = None
    _loss = None
    _draw = None
    _played = None
    _points = None
    _position = None
    _form = None

    def __init__(self, team: dict):
        dict.__init__(self, team)
        self._team = team
        self.id = self._team["id"]
        self.name = self._team["name"]
        self.code = self._team["code"]

        self.strength_overall_home = self._team["strength_overall_home"]
        self.strength_overall_away = self._team["strength_overall_away"]
        self.strength_attack_home = self._team["strength_attack_home"]
        self.strength_attack_away = self._team["strength_attack_away"]
        self.strength_defence_home = self._team["strength_defence_home"]
        self.strength_defence_away = self._team["strength_defence_away"]

        self.wins = self._team["win"]
        self.loss = self._team["loss"]
        self.draw = self._team["draw"]
        self.played = self._team["played"]
        self.points = self._team["points"]
        self.position = self._team["position"]
        self.form = self._team["form"]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError(f"Expected int, got {type(id)}")
        self._id = id

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code: int) -> None:
        if not isinstance(code, int):
            raise TypeError(f"Expected int, got {type(code)}")
        self._code = code

    @property
    def strength_overall_home(self):
        return self._strength_overall_home

    @strength_overall_home.setter
    def strength_overall_home(self, strength_overall_home: int) -> None:
        if not isinstance(strength_overall_home, int):
            raise TypeError(f"Expected int, got {type(strength_overall_home)}")
        self._strength_overall_home = strength_overall_home

    @property
    def strength_overall_away(self):
        return self._strength_overall_away

    @strength_overall_away.setter
    def strength_overall_away(self, strength_overall_away: int) -> None:
        if not isinstance(strength_overall_away, int):
            raise TypeError(f"Expected int, got {type(strength_overall_away)}")
        self._strength_overall_away = strength_overall_away

    @property
    def strength_attack_home(self):
        return self._strength_attack_home

    @strength_attack_home.setter
    def strength_attack_home(self, strength_attack_home: int) -> None:
        if not isinstance(strength_attack_home, int):
            raise TypeError(f"Expected int, got {type(strength_attack_home)}")
        self._strength_attack_home = strength_attack_home

    @property
    def strength_attack_away(self):
        return self._strength_attack_away

    @strength_attack_away.setter
    def strength_attack_away(self, strength_attack_away: int) -> None:
        if not isinstance(strength_attack_away, int):
            raise TypeError(f"Expected int, got {type(strength_attack_away)}")
        self._strength_attack_away = strength_attack_away

    @property
    def strength_defence_home(self):
        return self._strength_defence_home

    @strength_defence_home.setter
    def strength_defence_home(self, strength_defence_home: int) -> None:
        if not isinstance(strength_defence_home, int):
            raise TypeError(f"Expected int, got {type(strength_defence_home)}")
        self._strength_defence_home = strength_defence_home

    @property
    def strength_defence_away(self):
        return self._strength_defence_away

    @strength_defence_away.setter
    def strength_defence_away(self, strength_defence_away: int) -> None:
        if not isinstance(strength_defence_away, int):
            raise TypeError(f"Expected int, got {type(strength_defence_away)}")
        self._strength_defence_away = strength_defence_away

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins: int) -> None:
        if not isinstance(wins, int):
            raise TypeError(f"Expected int, got {type(wins)}")
        self._wins = wins

    @property
    def loss(self):
        return self._loss

    @loss.setter
    def loss(self, loss: int) -> None:
        if not isinstance(loss, int):
            raise TypeError(f"Expected int, got {type(loss)}")
        self._loss = loss

    @property
    def draw(self):
        return self._draw

    @draw.setter
    def draw(self, draw: int) -> None:
        if not isinstance(draw, int):
            raise TypeError(f"Expected int, got {type(draw)}")
        self._draw = draw

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points: int) -> None:
        if not isinstance(points, int):
            raise TypeError(f"Expected int, got {type(points)}")
        self._points = points

    @property
    def played(self):
        return self._played

    @played.setter
    def played(self, played: int) -> None:
        if not isinstance(played, int):
            raise TypeError(f"Expected int, got {type(played)}")
        self._played = played

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: int) -> None:
        if not isinstance(position, int):
            raise TypeError(f"Expected int, got {type(position)}")
        self._position = position

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, form: str) -> None:
        if not isinstance(form, str) and form is not None:
            raise TypeError(f"Expected str, got {type(form)}")
        self._form = form

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players: list[Player]) -> None:
        if not isinstance(players, list):
            raise TypeError(f"Expected list, got {type(players)}")
        self._players = players
