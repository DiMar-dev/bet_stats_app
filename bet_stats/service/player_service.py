from bet_stats.model.player import Player
from bet_stats.repository.player_repository import get_all_players, get_player_by_id, \
    get_player_by_name_surname
from bet_stats.repository import db_util


def get_all():
    return get_all_players()


def get_by_name_surname(name, surname):
    return get_player_by_name_surname(name, surname)


def save_player(data):
    player = Player(name=data['name'], surname=data['surname'], team_id=data['team'])
    db_util.save_data(player)


def update_player(data):
    player = get_player_by_id(data['id'])
    player.name = data['name']
    player.surname = data['surname']
    player.team_id = data['team']
    db_util.flush_and_commit_changes()


def delete_player(data):
    player = get_player_by_id(data['id'])
    db_util.delete_data(player)
