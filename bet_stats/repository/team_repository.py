from bet_stats.model.team import Team


def get_all_teams():
    return Team.query.all()


def get_team_by_id(obj_id):
    return Team.query.filter(Team.id == obj_id).first()


def get_team_by_short_name(short_name):
    return Team.query.filter(Team.short_name == short_name).first()


