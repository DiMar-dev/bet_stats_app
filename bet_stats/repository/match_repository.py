from sqlalchemy import and_, or_

from bet_stats.model.match import Match


def get_all_matches():
    return Match.query.order_by(Match.date_of_play.desc()).all()


def get_match_by_id(obj_id):
    return Match.query.filter(Match.id == obj_id).first()


def get_matches_by_home_team_id(team_id):
    return Match.query.filter(Match.team_home_id == team_id).all()


def get_matches_by_away_team_id(team_id):
    return Match.query.filter(Match.team_away_id == team_id).all()


def get_matches_by_both_teams(team_one, team_two):
    return Match.query.filter(or_(and_(Match.team_away_id == team_one,
                                       Match.team_home_id == team_two),
                                  and_(Match.team_away_id == team_two,
                                       Match.team_home_id == team_one))).all()


def get_matches_by_date_played(date):
    return Match.query.filter(Match.date_of_play == date)
