from bet_stats import db


class Player(db.Model):
    __tablename__ = 'player'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('public.team.id'), nullable=False)

    team = db.relationship('Team', foreign_keys=team_id)

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'team_id': self.team_id,
            'team': self.team.serialize
        }
