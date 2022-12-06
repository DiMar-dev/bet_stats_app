from bet_stats import db


class Team(db.Model):
    __tablename__ = 'team'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(3), nullable=False)
    full_name = db.Column(db.String(50), unique=True, nullable=False)

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'short_name': self.short_name,
            'full_name': self.full_name
        }

