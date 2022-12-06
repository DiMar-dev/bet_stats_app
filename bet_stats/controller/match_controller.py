from flask import render_template, request, redirect, url_for, jsonify

from bet_stats import app
from bet_stats.model.forms.match_forms import MatchUpdateForm, MatchCreateForm
from bet_stats.service import match_service, team_service


@app.route('/match', methods=['GET'])
def get_match():
    match_create = MatchCreateForm()
    match_create.team_home.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    match_create.team_away.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    match_update = MatchUpdateForm()
    match_update.team_home.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    match_update.team_away.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    return render_template('match.html',
                           matches=[i.serialize for i in match_service.get_all()],
                           match_create=match_create,
                           match_update=match_update)


@app.route('/match/add', methods=['POST'])
def create_match():
    data = request.form
    match_service.save_match(data)

    return redirect(url_for('get_match'))


@app.route('/match/update', methods=['POST'])
def update_match():
    data = request.form
    match_service.update_match(data)

    return redirect(url_for('get_match'))


@app.route('/match/delete', methods=['POST'])
def delete_match():
    data = request.form
    match_service.delete_match(data)

    return redirect(url_for('get_match'))
