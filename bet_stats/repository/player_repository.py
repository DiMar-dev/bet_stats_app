from sqlalchemy import and_

from bet_stats.model.player import Player


def get_all_players():
    return Player.query.all()


def get_player_by_id(obj_id):
    return Player.query.filter(Player.id == obj_id).first()


def get_players_by_team_id(team_id):
    return Player.query.filter(Player.team_id == team_id).first()


def get_player_by_name_surname(name, surname):
    return Player.query.filter(and_(Player.name == name,
                                    Player.surname == surname)).first()
