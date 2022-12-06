from flask import render_template

from bet_stats import app


@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')
