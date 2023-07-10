from src.model.team import Team

team = {
    'code': 94,
    'draw': 2,
    'form': None,
    'id': 4,
    'loss': 3,
    'name': 'TEST_TEAM',
    'played': 11,
    'points': 20,
    'position': 10,
    'short_name': 'BRE',
    'strength': 3,
    'team_division': None,
    'unavailable': False,
    'win': 6,
    'strength_overall_home': 1125,
    'strength_overall_away': 1205,
    'strength_attack_home': 1120,
    'strength_attack_away': 1220,
    'strength_defence_home': 1130,
    'strength_defence_away': 1190,
    'pulse_id': 130
}


def test_team():
    actual = Team(team)
    assert actual

