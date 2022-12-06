from flask import render_template, request, redirect, url_for, jsonify

from bet_stats import app
from bet_stats.model.forms.player_forms import PlayerUpdateForm, PlayerCreateForm
from bet_stats.service import team_service
from bet_stats.service.player_service import get_all, save_player, delete_player, update_player


@app.route('/player', methods=['GET'])
def get_player():
    player_create = PlayerCreateForm()
    player_create.team.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    player_update = PlayerUpdateForm()
    player_update.team.choices = [(item.id, item.short_name) for item in team_service.get_all()]
    return render_template('player.html',
                           players=[i.serialize for i in get_all()],
                           player_create=player_create,
                           player_update=player_update)


@app.route('/player/add', methods=['POST'])
def post_create_player():
    data = request.form
    save_player(data)

    return redirect(url_for('get_player'))


@app.route('/player/update', methods=['POST'])
def post_update_player():
    data = request.form
    update_player(data)

    return redirect(url_for('get_player'))


@app.route('/player/delete', methods=['POST'])
def post_delete_player():
    data = request.form
    delete_player(data)

    return redirect(url_for('get_player'))
