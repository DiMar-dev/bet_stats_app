from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, DateField


class MatchCreateForm(FlaskForm):
    team_home = SelectField(label='Home Team', choices=[])
    team_away = SelectField(label='Away Team', choices=[])
    team_home_score = IntegerField(label='Home team score')
    team_away_score = IntegerField(label='Away team score')
    date_of_play = DateField(label="Date of play")
    submit = SubmitField(label='Create')


class MatchUpdateForm(FlaskForm):
    id = IntegerField()
    team_home = SelectField(label='Home Team', choices=[])
    team_away = SelectField(label='Away Team', choices=[])
    team_home_score = IntegerField(label='Home team score')
    team_away_score = IntegerField(label='Away team score')
    date_of_play = DateField(label="Date of play")
    submit = SubmitField(label='Update')
