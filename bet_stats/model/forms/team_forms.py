from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class TeamCreateForm(FlaskForm):
    short_name = StringField(label='Short Name')
    full_name = StringField(label='Full Name')
    submit = SubmitField(label='Create')


class TeamUpdateForm(FlaskForm):
    id = IntegerField()
    short_name = StringField(label='Short Name')
    full_name = StringField(label='Full Name')
    submit = SubmitField(label='Update')