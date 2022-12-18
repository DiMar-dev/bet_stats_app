from sqlalchemy import and_, or_, true

from bet_stats.model.players_bet import PlayersBet


def get_all_players_bets():
    return PlayersBet.query.order_by(PlayersBet.creation_date.desc()).all()


def get_players_bet_by_id(obj_id):
    return PlayersBet.query.filter(PlayersBet.id == obj_id).first()


def get_matches_by_player_id(player_id):
    return PlayersBet.query.filter(PlayersBet.player_id == player_id)\
        .order_by(PlayersBet.creation_date.desc()).all()


def get_player_bets_by_result(result):
    return PlayersBet.query.filter(PlayersBet.bet_result == true).all()

