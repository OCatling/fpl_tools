class Player(dict):
    def __init__(self, player_dict: dict) -> None:
        dict.__init__(self, **player_dict)
        self.first_name = player_dict['first_name']
        self.second_name = player_dict['second_name']
        self.web_name = player_dict['web_name']
        self.id = player_dict['id']
        self.team = player_dict['team']
        self.position = player_dict['element_type']
        self.code = player_dict['code']
        self.squad_number = player_dict['squad_number']
        self.photo = player_dict['photo']
        self.news = player_dict['news']
        self.news_added = player_dict['news_added']

        self.team_code = player_dict['team_code']
        self.team_id = player_dict['team']

        self.starts = player_dict['starts']
        self.starts_per_90 = player_dict['starts_per_90']
        self.minutes = player_dict['minutes']
        self.goals_scored = player_dict['goals_scored']
        self.assists = player_dict['assists']
        self.clean_sheets = player_dict['clean_sheets']
        self.clean_sheets_per_90 = player_dict['clean_sheets_per_90']
        self.goals_conceded = player_dict['goals_conceded']
        self.goals_conceded_per_90 = player_dict['goals_conceded_per_90']
        self.own_goals = player_dict['own_goals']

        self.saves = player_dict['saves']
        self.saves_per_90 = player_dict['saves_per_90']
        self.penalties_saved = player_dict['penalties_saved']

        self.penalties_missed = player_dict['penalties_missed']
        self.penalties_order = player_dict['penalties_order']
        self.penalties_text = player_dict['penalties_text']

        self.corners_and_indirect_freekicks_order = player_dict['corners_and_indirect_freekicks_order']
        self.corners_and_indirect_freekicks_text = player_dict['corners_and_indirect_freekicks_text']

        self.direct_freekicks_order = player_dict['direct_freekicks_order']
        self.direct_freekicks_text = player_dict['direct_freekicks_text']

        self.yellow_cards = player_dict['yellow_cards']
        self.red_cards = player_dict['red_cards']

        self.expected_goals = player_dict['expected_goals']
        self.expected_goals_per_90 = player_dict['expected_goals_per_90']
        self.expected_assists = player_dict['expected_assists']
        self.expected_goal_involvements = player_dict['expected_goal_involvements']
        self.expected_goals_conceded = player_dict['expected_goals_conceded']

    def __str__(self) -> str:
        return f"{self.web_name} ({self.id})"
