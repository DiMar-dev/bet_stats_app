from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5433/bet_stats'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)


def db_config():
    db.session.configure(autoflush=False)


from bet_stats.controller import home_controller, team_controller, player_controller, match_controller, \
    players_bet_controller
