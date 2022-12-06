from flask import render_template, request, redirect, url_for, jsonify

from bet_stats import app
from bet_stats.model.forms.team_forms import TeamUpdateForm, TeamCreateForm
from bet_stats.service.team_service import get_all, save_team, delete_team, update_team


@app.route('/team', methods=['GET'])
def get():
    team_create = TeamCreateForm()
    team_update = TeamUpdateForm()
    return render_template('team_all.html',
                           teams=[i.serialize for i in get_all()],
                           team_create=team_create,
                           team_update=team_update)


@app.route('/team/add', methods=['POST'])
def post():
    data = request.form
    save_team(data)

    return redirect(url_for('get'))


@app.route('/team/update', methods=['POST'])
def put():
    data = request.form
    update_team(data)

    return redirect(url_for('get'))


@app.route('/team/delete', methods=['POST'])
def delete():
    data = request.form
    delete_team(data)

    return redirect(url_for('get'))
