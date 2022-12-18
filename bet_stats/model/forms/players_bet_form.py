from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, \
    SelectField, DateField, DecimalField, RadioField, TimeField


class PlayersBetCreateForm(FlaskForm):
    bet_match = SelectField(label='Match of bet', choices=[])
    player = SelectField(label='Player of bet', choices=[])
    actual_score = IntegerField(label='Actual score')
    margin_score = DecimalField(label='Score margin')
    bet_score = StringField(label='Bet score')
    bet_result = RadioField(label='Bet result', choices=[(True, 'Win'), (False, 'Lose')])
    play_time = TimeField(label='Play time', format="%M:%S")
    attempts = IntegerField(label='Attempts')
    realised_attempts = IntegerField(label='Realised attempts')
    # creation_date = DateField(label="Creation date")
    submit = SubmitField(label='Create')


class PlayersBetUpdateForm(FlaskForm):
    id_update = IntegerField()
    bet_match_update = SelectField(label='Match of bet', choices=[])
    player_update = SelectField(label='Player of bet', choices=[])
    actual_score_update = IntegerField(label='Actual score')
    margin_score_update = DecimalField(label='Score margin')
    bet_score_update = StringField(label='Bet score')
    bet_result_update = RadioField(label='Bet result', choices=[(True, 'Win'), (False, 'Lose')])
    play_time_update = TimeField(label='Play time', format="%M:%S")
    attempts_update = IntegerField(label='Attempts')
    realised_attempts_update = IntegerField(label='Realised attempts')
    # creation_date = DateField(label="Creation date")
    submit_update = SubmitField(label='Update')


class PlayersBetFilterByPlayerForm(FlaskForm):
    player = SelectField(label='Filter by player:', choices=[])
    submit = SubmitField(label='Filter')
