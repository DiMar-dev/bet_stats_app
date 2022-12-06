from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField


class PlayerCreateForm(FlaskForm):
    name = StringField(label='Name')
    surname = StringField(label='Surname')
    team = SelectField(label='Team', choices=[])
    submit = SubmitField(label='Create')


class PlayerUpdateForm(FlaskForm):
    id = IntegerField()
    name = StringField(label='Name')
    surname = StringField(label='Surname')
    team = SelectField(label='Team', choices=[])
    submit = SubmitField(label='Update')
