from flask import render_template

from app import app
from app.utils import Werkzeuge

baseDir = "C:\\Users\\acf040\\Downloads\\Data\\Data"
player = Werkzeuge.load_player(baseDir)

@app.route('/show')
def show():
    games = Werkzeuge.load_games(baseDir)
    return render_template('show.html', title='Show', game_list=games)

@app.route('/game/<gameID>')
def game(gameID):
    games = Werkzeuge.load_games(baseDir)
    game = games[int(gameID)]
    return render_template('single_game.html', title='Game', game=game, index=int(gameID), player=player)

@app.route('/')
def index():
    return render_template('contol_page.html', title='Game')