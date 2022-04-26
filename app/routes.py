import configparser
import json
import math
import os
from os.path import join

from flask import render_template, redirect, url_for, request

from app import app
from app.Models.Show import Show
from app.utils import Werkzeuge

config = configparser.ConfigParser()
config.read('.config')
baseDir = config['DEFAULT']["baseDir"]


@app.route('/')
def index():
    return redirect(url_for('game', game_id=0, round_id=0))


@app.route('/<game_id>/round/<round_id>', methods=['GET'])
def game(game_id, round_id):
    game_id_int = int(game_id)
    round_id_int = int(round_id)
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    temp_show, temp_game, rounds_list = Werkzeuge.get_rounds_as_list(games_json, game_id_int)
    Werkzeuge.write_to_dir_structure(baseDir, temp_show)

    if temp_game == [] and round_id_int != 0:
        return redirect(url_for('game', game_id=game_id, round_id=0))

    if len(rounds_list) <= 0:
        frage = []
    else:
        frage = rounds_list[round_id_int]

    game_score_0, game_score_1, round_score_0, round_score_1, win_list, cw = get_current_winner(temp_show, temp_game)

    minute = math.floor(temp_game.countdown / 60)
    min_string = str(minute).zfill(2)
    sec_string = str((temp_game.countdown-minute*60)).zfill(2)
    return render_template('control_page.html', title='Game', gameID=game_id_int, roundID=round_id_int,
                           titel=temp_game.title, desc=temp_game.description, rules=temp_game.rules,
                           game_score_0=game_score_0, game_score_1=game_score_1, round_score_0=round_score_0,
                           round_score_1=round_score_1, games_ammount=len(temp_show.games),
                           rounds_ammount=len(rounds_list), win_list=win_list, frage=frage, current_winning=cw,
                           bonusHome=temp_show.bonus_player_home, bonusGuest=temp_show.bonus_player_guest,
                           playerHome=temp_show.player_home, playerGuest=temp_show.player_guest,
                           countdown_enabled=temp_game.countdown_enabled, countdown_min=min_string,
                           countdown_sec=sec_string)


@app.route('/file')
def file():
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    return games_json


def get_current_winner(temp_show, temp_game):
    game_score_0 = temp_show.bonus_player_home
    game_score_1 = temp_show.bonus_player_guest
    for x in range(len(temp_show.games)):
        if temp_show.games[x].winner == 0:
            game_score_0 += x + 1
        elif temp_show.games[x].winner == 1:
            game_score_1 += x + 1
    round_score_0 = 0
    round_score_1 = 0
    for temp_round in temp_game.rounds:
        if temp_round.winner == 0:
            round_score_0 += 1
        elif temp_round.winner == 1:
            round_score_1 += 1
    cw = 0
    if round_score_0 < round_score_1:
        cw = 1
    elif round_score_0 == round_score_1:
        cw = -1

    win_list = [[], []]
    for game_dummy in temp_show.games:
        if game_dummy.winner == -1:
            win_list[0].append(0)
            win_list[1].append(0)
        elif game_dummy.winner == 0:
            win_list[0].append(1)
            win_list[1].append(-1)
        elif game_dummy.winner == 1:
            win_list[0].append(-1)
            win_list[1].append(1)
    return game_score_0, game_score_1, round_score_0, round_score_1, win_list, cw


@app.route('/game_score')
def game_score():
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    temp_show = Show.read_from_json(games_json)
    win_list = [[], []]
    player_guest_score = 0
    player_home_score = 0
    game_points = 1
    for game_dummy in temp_show.games:
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
                           player_guest_score=player_guest_score, player_home_name=temp_show.playerHome,
                           player_guest_name=temp_show.playerGuest, bonusHome=temp_show.bonusPlayerHome,
                           bonusGuest=temp_show.bonusPlayerGuest)


@app.route('/<game_id>/round/<round_id>/edit', methods=['GET'])
def game_edit(game_id, round_id):
    game_id_int = int(game_id)
    round_id_int = int(round_id)
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    temp_show, temp_game, rounds_list = Werkzeuge.get_rounds_as_list(games_json, game_id_int)
    Werkzeuge.write_to_dir_structure(baseDir, temp_show)

    if len(rounds_list) <= 0:
        no_rounds = True
    else:
        no_rounds = False

    if len(rounds_list) <= 0 or len(rounds_list[round_id_int]) <= 1:
        frage = [0, "frage", ["antwortA", "antwortB", "antwortC", "antwortD"], 2]
        no_question = True
    else:
        frage = rounds_list[round_id_int]
        no_question = False

    game_score_0, game_score_1, round_score_0, round_score_1, win_list, cw = get_current_winner(temp_show, temp_game)

    if temp_game.countdown == -1:
        countdown = 10
    else:
        countdown = temp_game.countdown
    round_amount = len(temp_game.rounds)
    if round_amount == 0:
        round_amount = 1

    return render_template('control_page_edit.html', title='Game', gameID=game_id_int,
                           roundID=round_id_int, titel=temp_game.title, desc=temp_game.description,
                           rules=temp_game.rules, game_score_0=game_score_0, game_score_1=game_score_1,
                           round_score_0=round_score_0, round_score_1=round_score_1, game_amount=len(temp_show.games),
                           round_amount=round_amount, win_list=win_list, frage=frage, current_winning=cw,
                           bonusHome=temp_show.bonus_player_home, bonusGuest=temp_show.bonus_player_guest,
                           playerHome=temp_show.player_home, playerGuest=temp_show.player_guest,
                           countdown_enabled=temp_game.countdown_enabled, countdown=countdown, noquestion=no_question,
                           norounds=no_rounds)


@app.route('/<game_id>/round/<round_id>/questions', methods=['GET'])
def questions(game_id, round_id):
    game_id_int = int(game_id)
    round_id_int = int(round_id)
    games_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    temp_show, temp_game, rounds_list = Werkzeuge.get_rounds_as_list(games_json, game_id_int)
    question = ""
    answers = []
    correct = -1
    if len(rounds_list) > round_id_int:
        if len(rounds_list[round_id_int]) > 1:
            Werkzeuge.write_to_dir_structure(baseDir, temp_show)
            question = rounds_list[round_id_int][1]
            answers = []
            for i in range(len(rounds_list[round_id_int][2])):
                answers.append([i, rounds_list[round_id_int][2][i]])
            correct = rounds_list[round_id_int][3]
    games_amount = len(temp_show.games)
    round_amount = len(rounds_list)
    return render_template('question.html', question=question, answers=answers, gameID=game_id_int,
                           roundID=round_id_int, games_ammount=games_amount, round_ammount=round_amount,
                           correct=correct)


@app.route('/<game_id>/round/<round_id>', methods=['POST'])
def game_post(game_id, round_id):
    show_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    return_json = json.loads(request.form["return_value"])
    if return_json["method"] == "change_game_winner":
        if show_json["games"][return_json["game"]]["winner"] == return_json["player"]:
            show_json["games"][return_json["game"]]["winner"] = -1
        else:
            show_json["games"][return_json["game"]]["winner"] = return_json["player"]
    if return_json["method"] == "change_round_winner":
        if show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] == return_json["player"]:
            show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] = -1
        else:
            show_json["games"][return_json["game"]]["Rounds"][return_json["round"]]["winner"] = return_json["player"]

        score_dir = join(baseDir, "Score")
        if not os.path.isdir(score_dir):
            os.mkdir(score_dir)

        round_score_home = 0
        round_score_guest = 0
        rounds = show_json["games"][return_json["game"]]["Rounds"]
        for temp_round in rounds:
            if temp_round["winner"] == 0:
                round_score_home += 1
            elif temp_round["winner"] == 1:
                round_score_guest += 1

        Werkzeuge.write_line_to_file(score_dir, "Points.txt",
                                     str(round_score_home) + " : " + str(round_score_guest))

    if return_json["method"] == "addBonus":
        if return_json["player"] == 0:
            show_json["bonus_player_home"] += return_json["bonus"]
        elif return_json["player"] == 1:
            show_json["bonus_player_guest"] += return_json["bonus"]

    Werkzeuge.save_show(baseDir, "GameShow1.json", show_json)
    show = Show.read_from_json(show_json)
    Werkzeuge.write_to_dir_structure(baseDir, show)
    return redirect(url_for('game', game_id=game_id, round_id=round_id))


@app.route('/<game_id>/round/<round_id>/edit', methods=['POST'])
def game_edit_post(game_id, round_id):
    show_json = Werkzeuge.load_games(baseDir, "GameShow1.json")
    return_json = json.loads(request.form["return_value"])

    show_json["player_home"] = return_json["name_home"]
    show_json["player_guest"] = return_json["name_guest"]

    if len(show_json["games"]) < return_json["amount_of_games"]:
        for i in range(return_json["amount_of_games"]):
            if len(show_json["games"]) <= i:
                show_json["games"].append(
                    {
                        "Title": "Spiel " + str(i+1),
                        "Description": "desc.",
                        "Rules": "Regeln",
                        "Countdown": -1,
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

    if return_json["has_rounds"]:
        if len(current_game["Rounds"]) < return_json["amount_of_rounds"]:
            for i in range(return_json["amount_of_rounds"]):
                if len(current_game["Rounds"]) <= i:
                    current_game["Rounds"].append({"winner": -1})
        elif len(current_game["Rounds"]) > return_json["amount_of_rounds"]:
            current_game["Rounds"] = current_game["Rounds"][:return_json["amount_of_rounds"]]

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
            current_game["Questions"][int(round_id)] = {
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

    show = Show.read_from_json(show_json)
    Werkzeuge.write_to_dir_structure(baseDir, show)
    return redirect(url_for('game', game_id=game_id, round_id=round_id))
