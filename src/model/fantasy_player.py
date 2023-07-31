from src.model.player import Player


class FantasyPlayer(Player):
    def __init__(self, fantasy_player_dict: dict) -> None:
        super().__init__(fantasy_player_dict)

        self.special = fantasy_player_dict['special']
        self.status = fantasy_player_dict['status']

        self.form = fantasy_player_dict['form']
        self.form_rank = fantasy_player_dict['form_rank']
        self.form_rank_type = fantasy_player_dict['form_rank_type']

        self.event_points = fantasy_player_dict['event_points']
        self.total_points = fantasy_player_dict['total_points']
        self.bps = fantasy_player_dict['bps']
        self.bonus = fantasy_player_dict['bonus']
        self.points_per_game = fantasy_player_dict['points_per_game']
        self.points_per_game_rank = fantasy_player_dict['points_per_game_rank']
        self.points_per_game_rank_type = fantasy_player_dict['points_per_game_rank_type']

        self.value_form = fantasy_player_dict['value_form']
        self.value_season = fantasy_player_dict['value_season']

        self.selected_by_percent = fantasy_player_dict['selected_by_percent']
        # self.selected_by_percent_rank = fantasy_player_dict['selected_by_percent_rank']
        # self.selected_by_percent_rank_type = fantasy_player_dict['selected_by_percent_rank_type']

        self.ep_this = fantasy_player_dict['ep_this']
        self.ep_next = fantasy_player_dict['ep_next']
        self.in_dreamteam = fantasy_player_dict['in_dreamteam']
        self.dreamteam_count = fantasy_player_dict['dreamteam_count']

        self.news = fantasy_player_dict['news']
        self.news_added = fantasy_player_dict['news_added']
        self.chance_of_playing_next_round = fantasy_player_dict['chance_of_playing_next_round']
        self.chance_of_playing_this_round = fantasy_player_dict['chance_of_playing_this_round']

        self.transfers_in = fantasy_player_dict['transfers_in']
        self.transfers_in_event = fantasy_player_dict['transfers_in_event']
        self.transfers_out = fantasy_player_dict['transfers_out']
        self.transfers_out_event = fantasy_player_dict['transfers_out_event']

        self.now_cost = fantasy_player_dict['now_cost']
        self.now_cost_rank = fantasy_player_dict['now_cost_rank']
        self.now_cost_rank_type = fantasy_player_dict['now_cost_rank_type']

        self.cost_change_event = fantasy_player_dict['cost_change_event']
        self.cost_change_event_fall = fantasy_player_dict['cost_change_event_fall']
        self.cost_change_start = fantasy_player_dict['cost_change_start']
        self.cost_change_start_fall = fantasy_player_dict['cost_change_start_fall']

    class ICTIndex:
        def __init__(self, ict_dict) -> None:
            self.influence = ict_dict['influence']
            self.creativity = ict_dict['creativity']
            self.threat = ict_dict['threat']
            self.influence_rank = ict_dict['influence_rank']
            self.influence_rank_type = ict_dict['influence_rank_type']
            self.creativity_rank = ict_dict['creativity_rank']
            self.creativity_rank_type = ict_dict['creativity_rank_type']
            self.threat_rank = ict_dict['threat_rank']
            self.threat_rank_type = ict_dict['threat_rank_type']
            self.ict_index = ict_dict['ict_index']
            self.ict_index_rank = ict_dict['ict_index_rank']
            self.ict_index_rank_type = ict_dict['ict_index_rank_type']
