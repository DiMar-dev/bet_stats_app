import datetime

from bet_stats import db


class Match(db.Model):
    __tablename__ = 'match_'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    team_home_id = db.Column(db.Integer, db.ForeignKey('public.team.id'), nullable=False)
    team_away_id = db.Column(db.Integer, db.ForeignKey('public.team.id'), nullable=False)
    team_home_score = db.Column(db.SmallInteger, nullable=False)
    team_away_score = db.Column(db.SmallInteger, nullable=False)
    date_of_play = db.Column(db.Date, nullable=False)

    team_home = db.relationship('Team', foreign_keys=team_home_id)
    team_away = db.relationship('Team', foreign_keys=team_away_id)

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'team_home_id': self.team_home_id,
            'team_home': self.team_home.serialize,
            'team_away_id': self.team_away_id,
            'team_away': self.team_away.serialize,
            'team_home_score': self.team_home_score,
            'team_away_score': self.team_away_score,
            'date_of_play': self.date_of_play.strftime('%d-%m-%Y')
        }
