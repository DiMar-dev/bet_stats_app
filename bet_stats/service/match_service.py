from bet_stats.model.match import Match
from bet_stats.repository.match_repository import get_all_matches, get_match_by_id
from bet_stats.repository import db_util
from datetime import datetime


def get_all():
    return get_all_matches()


def save_match(data):
    match = Match(team_home_id=data['team_home'],
                  team_away_id=data['team_away'],
                  team_home_score=data['team_home_score'],
                  team_away_score=data['team_away_score'],
                  date_of_play=datetime.now())
    db_util.save_data(match)


def update_match(data):
    match = get_match_by_id(data['id'])
    match.team_home_id = data['team_home']
    match.team_away_id = data['team_away']
    match.team_home_score = data['team_home_score']
    match.team_away_score = data['team_away_score']
    match.date_of_play = data['date_of_play']
    db_util.flush_and_commit_changes()


def delete_match(data):
    match = get_match_by_id(data['id'])
    db_util.delete_data(match)
