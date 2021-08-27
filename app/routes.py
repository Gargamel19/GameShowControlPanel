import configparser
import json
import math

from flask import render_template, redirect, url_for, request

from app import app
from app.Models.Show import Show
from app.utils import Werkzeuge

config = configparser.ConfigParser()
config.read('.config')
baseDir = config['DEFAULT']["baseDir"]

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

    if game == [] and roundID_int != 0:
        return redirect(url_for('game', gameID=gameID, roundID=0))

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
    if game != []:
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
    min_string = str(math.floor(game.countdown/60)).zfill(2)
    min = math.floor(game.countdown/60)
    sec_string = str((game.countdown-min*60)).zfill(2)
    sec = str((game.countdown-min*60)).zfill(2)
    return render_template('contol_page.html', title='Game', gameID=gameID_int,
                            roundID=roundID_int, titel=game.title, desc=game.description, rules=game.rules,
                            game_score_0=game_score_0, game_score_1=game_score_1, round_score_0=round_score_0,
                            round_score_1=round_score_1, games_ammount=len(show.games),
                            rounds_ammount=len(rounds_list), win_list=win_list,
                            frage=frage, current_winning=cw, bonusHome=show.bonusPlayerHome,
                            bonusGuest=show.bonusPlayerGuest, playerHome=show.playerHome, playerGuest=show.playerGuest,
                            stopwatch_enabled=game.stopwatch_enabled, countdown_enabled=game.countdown_enabled,
                            countdown_min=min_string, countdown_sec=sec_string)


@app.route('/file')
def file():
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    return games_json
@app.route('/game_score')
def game_score():
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    show = Show.readFromJson(games_json)
    win_list = [[], []]
    player_guest_score = 0
    player_home_score = 0
    game_points = 1
    for game_dummy in show.games:
        if game_dummy.winner == -1:
            win_list[0].append(0)
            win_list[1].append(0)
        elif game_dummy.winner == 0:
            player_home_score += game_points
            win_list[0].append(1)
            win_list[1].append(-1)
        elif game_dummy.winner == 1:
            player_guest_score += game_points
            win_list[0].append(-1)
            win_list[1].append(1)
        game_points += 1

    return render_template('score_page.html', title='Game', win_list=win_list, player_home_score=player_home_score,
                           player_guest_score=player_guest_score, player_home_name=show.playerHome.upper(),
                           player_guest_name=show.playerGuest.upper(), bonusHome=show.bonusPlayerHome,
                           bonusGuest=show.bonusPlayerGuest)


@app.route('/<gameID>/round/<roundID>/edit', methods=['GET'])
def game_edit(gameID, roundID):
    gameID_int = int(gameID)
    roundID_int = int(roundID)
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    show, game, rounds_list = Werkzeuge.get_rounds_as_list(games_json, gameID_int)
    Werkzeuge.write_to_dir_structure(baseDir, show)

    if len(rounds_list) <= 0:
        norounds = True
    else:
        norounds = False

    if len(rounds_list) <= 0 or len(rounds_list[roundID_int]) <= 1:

        frage = [0, "frage", ["antwortA", "antwortB", "antwortC", "antwortD"], 2]
        noquestion = True

    else:
        frage = rounds_list[roundID_int]
        noquestion = False

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

    countdown = -1
    if game.countdown == -1:
        countdown = 10
    else:
        countdown = game.countdown

    round_amount = len(rounds_list)
    if len(rounds_list) == 0:
        round_amount += 1

    return render_template('contol_page_edit.html', title='Game', gameID=gameID_int,
                            roundID=roundID_int, titel=game.title, desc=game.description, rules=game.rules,
                            game_score_0=game_score_0, game_score_1=game_score_1, round_score_0=round_score_0,
                            round_score_1=round_score_1, game_amount=len(show.games),
                            round_amount=round_amount, win_list=win_list,
                            frage=frage, current_winning=cw, bonusHome=show.bonusPlayerHome,
                            bonusGuest=show.bonusPlayerGuest, playerHome=show.playerHome, playerGuest=show.playerGuest,
                            stopwatch_enabled=game.stopwatch_enabled, countdown_enabled=game.countdown_enabled,
                            countdown=countdown, noquestion=noquestion, norounds=norounds)


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
    show = Show.readFromJson(show_json)
    Werkzeuge.write_to_dir_structure(baseDir, show)
    return redirect(url_for('game', gameID=gameID, roundID=roundID))


@app.route('/<gameID>/round/<roundID>/edit', methods=['POST'])
def game_edit_post(gameID, roundID):
    show_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    show = Show.readFromJson(show_json)
    return_json = json.loads(request.form["return_value"])

    show_json["playerHome"] = return_json["nameHome"]
    show_json["playerGuest"] = return_json["nameGuest"]


    if len(show_json["games"]) < return_json["amount_of_games"]:
        for i in range(return_json["amount_of_games"]):
            if len(show_json["games"]) <= i:
                show_json["games"].append(
                    {
                        "Title": "Spiel " + str(i+1),
                        "Description": "desc.",
                        "Rules": "Regeln",
                        "Countdown": -1,
                        "Stopwatch": False,
                        "CurrentRound": 0,
                        "Rounds": [],
                        "ScoreHome": 0,
                        "ScoreGuest": 0,
                        "winner": -1
                    }
                )
    elif len(show_json["games"]) > return_json["amount_of_games"]:
        show_json["games"] = show_json["games"][:return_json["amount_of_games"]]

    current_game = show_json["games"][return_json["game_number"]]
    current_game["Title"] = return_json["title"]
    current_game["Description"] = return_json["description"]
    current_game["Rules"] = return_json["rules"]
    current_game["Countdown"] = return_json["countdown_value"]
    current_game["Stopwatch"] = return_json["stopwatch"]

    if return_json["has_rounds"]:
        if len(current_game["Rounds"]) < return_json["amount_of_rounds"]:
            for i in range(return_json["amount_of_rounds"]):
                if len(current_game["Rounds"]) <= i:
                    current_game["Rounds"].append({"winner": -1})

        if return_json["has_questions"]:
            if "Questions" not in current_game:
                current_game["Questions"] = []
            if len(current_game["Questions"]) < return_json["amount_of_rounds"]:
                for i in range(return_json["amount_of_rounds"]):
                    if len(current_game["Questions"]) <= i:
                        current_game["Questions"].append({
                                "question": "Wer schrieb das Buch 'Die Blechtrommel'?",
                                "content": [
                                    "Jens Nowotny",
                                    "Günther Grass",
                                    "Marco bode",
                                    "Carsten Jancker"
                                ],
                                "correct": 1
                            }
                        )
            current_game["Questions"][int(roundID)] = {
                "question": return_json["frage"][0],
                "content": return_json["frage"][1],
                "correct": return_json["frage"][2],
            }
        else:
            current_game["Questions"] = []
    else:
        current_game["Rounds"] = []
        current_game["Questions"] = []

    Werkzeuge.save_show(baseDir, "GameShow1.json", show_json)

    show = Show.readFromJson(show_json)
    Werkzeuge.write_to_dir_structure(baseDir, show)
    return redirect(url_for('game', gameID=gameID, roundID=roundID))
