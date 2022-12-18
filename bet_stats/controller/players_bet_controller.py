from flask import render_template, request, redirect, url_for, jsonify

from bet_stats import app
from bet_stats.model.forms.players_bet_form import PlayersBetUpdateForm, PlayersBetCreateForm, \
    PlayersBetFilterByPlayerForm
from bet_stats.service import match_service, player_service, players_bet_service


@app.route('/players_bet', defaults={'player_id': None}, methods=['GET'])
@app.route('/players_bet/<player_id>', methods=['GET'])
def get_player_bets(player_id):
    player_bets = players_bet_service.get_by_player(player_id) \
        if player_id else players_bet_service.get_all()
    players_bet_create = PlayersBetCreateForm()
    players_bet_create.bet_match.choices = [(item.id, "".join([item.team_home.short_name,
                                                               ':',
                                                               item.team_away.short_name,
                                                               '/',
                                                               item.date_of_play.strftime('%d-%m-%Y')]))
                                            for item in match_service.get_all()]
    players_bet_create.player.choices = [(item.id, "".join([item.name,
                                                            ' ',
                                                            item.surname]))
                                         for item in player_service.get_all()]
    players_bet_update = PlayersBetUpdateForm()
    players_bet_update.bet_match_update.choices = players_bet_create.bet_match.choices
    players_bet_update.player_update.choices = players_bet_create.player.choices
    players_bet_filter = PlayersBetFilterByPlayerForm()
    players_bet_filter.player.choices = players_bet_create.player.choices
    return render_template('players_bet.html',
                           player_bets=[i.serialize for i in player_bets],
                           players_bet_create=players_bet_create,
                           players_bet_update=players_bet_update,
                           players_bet_filter=players_bet_filter)


@app.route('/players_bet/add', methods=['POST'])
def create_player_bets():
    data = request.form
    players_bet_service.save_match(data)

    return redirect(url_for('get_player_bets'))


@app.route('/players_bet/update', methods=['POST'])
def update_player_bets():
    data = request.form
    players_bet_service.update_match(data)

    return redirect(url_for('get_player_bets'))


@app.route('/players_bet/delete', methods=['POST'])
def delete_player_bets():
    data = request.form
    players_bet_service.delete_match(data)

    return redirect(url_for('get_player_bets'))


@app.route('/players_bet/filter', methods=['POST'])
def filter_player_bets():
    data = request.form
    player_id = data['player']
    url = url_for('get_player_bets') + '/' + player_id

    return redirect(url)
