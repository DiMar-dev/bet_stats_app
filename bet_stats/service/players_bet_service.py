from bet_stats.model.players_bet import PlayersBet
from bet_stats.repository.players_bet_repository import get_all_players_bets, get_players_bet_by_id, \
    get_matches_by_player_id
from bet_stats.repository import db_util
from datetime import datetime


def get_all():
    return get_all_players_bets()


def get_by_player(player_id):
    return get_matches_by_player_id(player_id)


def save_match(data):
    players_bet = PlayersBet(bet_match_id=data['bet_match'],
                             player_id=data['player'],
                             actual_score=data['actual_score'],
                             margin_score=data['margin_score'],
                             bet_score=data['bet_score'],
                             bet_result=1 if data['bet_result'] == 'True' else 0,
                             play_time=data['play_time'],
                             attempts=data['attempts'],
                             realised_attempts=data['realised_attempts'],
                             creation_date=datetime.now())
    db_util.save_data(players_bet)


def update_match(data):
    player_bet = get_players_bet_by_id(data['id_update'])
    player_bet.bet_match_id = data['bet_match_update']
    player_bet.player_id = data['player_update']
    player_bet.actual_score = data['actual_score_update']
    player_bet.margin_score = data['margin_score_update']
    player_bet.bet_score = data['bet_score_update']
    player_bet.bet_result = True if data['bet_result_update'] == 'True' else False
    player_bet.play_time = data['play_time_update']
    player_bet.attempts = data['attempts_update']
    player_bet.realised_attempts = data['realised_attempts_update']
    db_util.flush_and_commit_changes()


def delete_match(data):
    player_bet = get_players_bet_by_id(data['id'])
    db_util.delete_data(player_bet)
