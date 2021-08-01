from flask import render_template, redirect, url_for

from app import app
from app.utils import Werkzeuge

baseDir = "D:\\Projects\\GameshowGames\\Data"
player = Werkzeuge.load_player(baseDir)

@app.route('/show')
def show():
    games = Werkzeuge.load_games(baseDir)
    return render_template('show.html', title='Show', game_list=games)

@app.route('/')
def index():
    return redirect(url_for('game', gameID=0, roundID=0))

@app.route('/<gameID>/round/<roundID>')
def game(gameID, roundID):
    games = Werkzeuge.load_games(baseDir)
    game = games[int(gameID)]
    #TODO: WINNER
    winner = 3
    frage1 = ["frage", ["Antwort1", "Antwort2", "Antwort3", "Antwort4"], 1]
    frage2 = ["frage", ["Antwort1", "Antwort2", "Antwort3", "Antwort4"], 3]
    frage3 = ["frage", ["Antwort1", "Antwort2", "Antwort3", "Antwort4"], 0]
    fragen = [frage1, frage2, frage3]
    return render_template('contol_page.html', title='Game', gameID=int(gameID),
                           roundID=int(roundID), titel=game[0], desc=game[1], rules=game[2], winner=winner,
                           round_score_0=1, round_score_1=4, frage=fragen[int(roundID)])
