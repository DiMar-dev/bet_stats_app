from bet_stats.model.team import Team
from bet_stats.repository.team_repository import get_all_teams, get_team_by_short_name, get_team_by_id
from bet_stats.repository import db_util


def get_all():
    return get_all_teams()


def get_by_short_name(short_name):
    return get_team_by_short_name(short_name)


def save_team(data):
    team = Team(short_name=data['short_name'], full_name=data['full_name'])
    db_util.save_data(team)


def update_team(data):
    team = get_team_by_id(data['id'])
    team.short_name = data['short_name']
    team.full_name = data['full_name']
    db_util.flush_and_commit_changes()


def delete_team(data):
    team = get_team_by_id(data['id'])
    db_util.delete_data(team)
