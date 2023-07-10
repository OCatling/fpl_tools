class Team:
    def __init__(self, team):
        self._team = team
        self._id = self._team["id"]
        self._name = self._team["name"]
        self._code = self._team["code"]

        self._strength_overall_home = self._team["strength_overall_home"]
        self._strength_overall_away = self._team["strength_overall_away"]
        self._strength_attack_home = self._team["strength_attack_home"]
        self._strength_attack_away = self._team["strength_attack_away"]
        self._strength_defence_home = self._team["strength_defence_home"]
        self._strength_defence_away = self._team["strength_defence_away"]

        self._wins = self._team["win"]
        self._loss = self._team["loss"]
        self._draw = self._team["draw"]
        self._played = self._team["played"]
        self._points = self._team["points"]
        self._position = self._team["position"]
        self._form = self._team["form"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id

    @property
    def code(self):
        return self._code

    @property
    def strength_overall_home(self):
        return self._strength_overall_home

    @strength_overall_home.setter
    def strength_overall_home(self, strength_overall_home: int) -> None:
        self._strength_overall_home = strength_overall_home

    @property
    def strength_overall_away(self):
        return self._strength_overall_away

    @strength_overall_away.setter
    def strength_overall_away(self, strength_overall_away: int) -> None:
        self._strength_overall_away = strength_overall_away

    @property
    def strength_attack_home(self):
        return self._strength_attack_home

    @strength_attack_home.setter
    def strength_attack_home(self, strength_attack_home: int) -> None:
        self._strength_attack_home = strength_attack_home

    @property
    def strength_attack_away(self):
        return self._strength_attack_away

    @strength_attack_away.setter
    def strength_attack_away(self, strength_attack_away: int) -> None:
        self._strength_attack_away = strength_attack_away

    @property
    def strength_defence_home(self):
        return self._strength_defence_home

    @strength_defence_home.setter
    def strength_defence_home(self, strength_defence_home: int) -> None:
        self._strength_defence_home = strength_defence_home

    @property
    def strength_defence_away(self):
        return self._strength_defence_away

    @strength_defence_away.setter
    def strength_defence_away(self, strength_defence_away: int) -> None:
        self._strength_defence_away = strength_defence_away

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins: int) -> None:
        self._wins = wins

    @property
    def loss(self):
        return self._loss

    @loss.setter
    def loss(self, loss: int) -> None:
        self._loss = loss

    @property
    def draw(self):
        return self._draw

    @draw.setter
    def draw(self, draw: int) -> None:
        self._draw = draw

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points: int) -> None:
        self._points = points
