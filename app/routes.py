import configparser
import json

from flask import render_template, redirect, url_for, request

from app import app
from app.Models.Show import Show
from app.utils import Werkzeuge

config = configparser.ConfigParser()
config.read('.config')
baseDir = config['DEFAULT']["baseDir"]


@app.route('/show')
def show():
    games = Werkzeuge.load_games(baseDir)
    return render_template('show.html', title='Show', game_list=games)


@app.route('/')
def index():
    return redirect(url_for('game', gameID=0, roundID=0))


@app.route('/<gameID>/round/<roundID>', methods=['GET'])
def game(gameID, roundID):
    gameID_int = int(gameID)
    roundID_int = int(roundID)
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    show, game, rounds_list = Werkzeuge.get_rounds_as_list(games_json, gameID_int)
    Werkzeuge.write_to_dir_structure(baseDir, show)

    if len(rounds_list) <= 0:
        frage = []
    else:
        frage = rounds_list[roundID_int]

    game_score_0 = show.bonusPlayerHome
    game_score_1 = show.bonusPlayerGuest
    for x in range(len(show.games)):
        if show.games[x].winner == 0:
            game_score_0 += x+1
        elif show.games[x].winner == 1:
            game_score_1 += x+1

    round_score_0 = 0
    round_score_1 = 0
    for round in game.rounds:
        if round.winner == 0:
            round_score_0 += 1
        elif round.winner == 1:
            round_score_1 += 1

    if round_score_0 > round_score_1:
        cw = 0
    elif round_score_0 < round_score_1:
        cw = 1
    elif round_score_0 == round_score_1:
        cw = -1

    win_list = [[], []]
    for game_dummy in show.games:
        if game_dummy.winner == -1:
            win_list[0].append(0)
            win_list[1].append(0)
        elif game_dummy.winner == 0:
            win_list[0].append(1)
            win_list[1].append(-1)
        elif game_dummy.winner == 1:
            win_list[0].append(-1)
            win_list[1].append(1)
    return render_template('contol_page.html', title='Game', gameID=gameID_int,
                            roundID=roundID_int, titel=game.title, desc=game.description, rules=game.rules,
                            game_score_0=game_score_0, game_score_1=game_score_1, round_score_0=round_score_0,
                           round_score_1=round_score_1, games_ammount=len(show.games),
                            rounds_ammount=len(rounds_list), win_list=win_list,
                            frage=frage, current_winning=cw, bonusHome=show.bonusPlayerHome,
                            bonusGuest=show.bonusPlayerGuest, playerHome=show.playerHome, playerGuest=show.playerGuest,
                            stopwatch_enabled=game.stopwatch_enabled, countdown_enabled=game.countdown_enabled,
                            countdown=game.countdown)

@app.route('/<gameID>/round/<roundID>', methods=['POST'])
def game_post(gameID, roundID):
    show_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    show = Show.readFromJson(show_json)
    return_json = json.loads(request.form["return_value"])
    if return_json["method"] == "cahage_game_winner":
        if show_json["games"][return_json["game"]]["winner"] == return_json["player"]:
            show_json["games"][return_json["game"]]["winner"] = -1
        else:
            show_json["games"][return_json["game"]]["winner"] = return_json["player"]
    if return_json["method"] == "cahage_round_winner":
        if show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] == return_json["player"]:
            show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] = -1
        else:
            show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] = return_json["player"]
    if return_json["method"] == "addBonus":
        if return_json["player"] == 0:
            show_json["bonusPlayerHome"] += return_json["bonus"]
        elif return_json["player"] == 1:
            show_json["bonusPlayerGuest"] += return_json["bonus"]

    Werkzeuge.save_show(baseDir, "GameShow1.json", show_json)
    Werkzeuge.write_to_dir_structure(baseDir, show)
    return redirect(url_for('game', gameID=gameID, roundID=roundID))
