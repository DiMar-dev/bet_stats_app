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
    id = IntegerField()
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
    submit = SubmitField(label='Update')
