from bet_stats import db


class PlayersBet(db.Model):
    __tablename__ = 'players_bet'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    bet_match_id = db.Column(db.Integer, db.ForeignKey('public.match_.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('public.player.id'), nullable=False)
    actual_score = db.Column(db.SmallInteger, nullable=False)
    margin_score = db.Column(db.Numeric, nullable=False)
    bet_score = db.Column(db.String(1), nullable=False)
    bet_result = db.Column(db.Boolean, nullable=False)
    play_time = db.Column(db.Interval, nullable=False)
    attempts = db.Column(db.SmallInteger, nullable=False)
    realised_attempts = db.Column(db.SmallInteger, nullable=False)
    creation_date = db.Column(db.Date)

    bet_match = db.relationship('Match', foreign_keys=bet_match_id)
    player = db.relationship('Player', foreign_keys=player_id)

    @property
    def serialize(self) -> dict:
        return {
            'id': self.id,
            'bet_match_id': self.bet_match_id,
            'bet_match': self.bet_match.serialize,
            'player_id': self.player_id,
            'player': self.player.serialize,
            'actual_score': self.actual_score,
            'margin_score': str(self.margin_score),
            'bet_score': self.bet_score,
            'bet_result': 'True' if self.bet_result else 'False',
            'play_time': str(self.play_time),
            'attempts': self.attempts,
            'realised_attempts': self.realised_attempts,
            'creation_date': self.creation_date.strftime('%d-%m-%Y')
        }
