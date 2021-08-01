import json
import os
from os import listdir
from os.path import join

from app.Models.QuestionRound import QuestionRound
from app.Models.Show import Show


class Werkzeuge:

    @staticmethod
    def save_show(base_dir, game_show_name, show_json):
        games_dir = join(base_dir, game_show_name)
        with open(games_dir, "w+", encoding="utf-8") as file:
            file.writelines(json.dumps(show_json))


    @staticmethod
    def load_games(base_dir, game_show_name):
        games_dir = join(base_dir, game_show_name)
        with open(games_dir, "r", encoding="utf-8") as file:

            # read Json file
            json_string = ""
            json_string_lines = file.readlines()
            for line in json_string_lines:
                json_string += line
            return json.loads(json_string)

    @staticmethod
    def get_rounds_as_list(questions_json, index):
        show = Show.readFromJson(questions_json)
        game = show.games[index]
        rounds = []
        for round in game.rounds:
            if type(round) is QuestionRound:
                rounds.append([round.winner, round.question, round.content, round.correct])
            else:
                rounds.append([round.winner])
        return show, game, rounds





    @staticmethod
    def load_games2(base_dir):
        games = []
        games_dir = join(base_dir, "Games")
        gmaes_dirs_list = listdir(games_dir)
        for game_folder_path in gmaes_dirs_list:
            game = []
            if game_folder_path.startswith("Game "):
                game_dir = join(games_dir, game_folder_path)
                title_file = join(game_dir, "Title.txt")
                with open(title_file, "r") as file:
                    title = file.readlines()[0]
                    game.append(title)

                description_file = join(game_dir, "Description.txt")
                with open(description_file, "r") as file:
                    description = file.readlines()
                    for x in range(len(description)):
                        description[x] = description[x].replace("\n", "")
                    game.append(description)

                rules_file = join(game_dir, "Rules.txt")
                with open(rules_file, "r") as file:
                    rules = file.readlines()
                    for x in range(len(rules)):
                        rules[x] = rules[x].replace("\n", "")
                    game.append(rules)
                if "Questions.json" in os.listdir(game_dir):
                    questions_file = join(game_dir, "Questions.json")
                    with open(questions_file, "r", encoding="utf-8") as file:
                        questions = []
                        questions_json_string = ""
                        questions_json_string_lines = file.readlines()
                        for line in questions_json_string_lines:
                            questions_json_string += line
                        questions_json = json.loads(questions_json_string)
                        for element in questions_json:
                            questions.append([element["question"], element["content"], element["correct"]])
                        game.append(questions)
                else:
                    game.append([])
                games.append(game)
        return games

    @staticmethod
    def load_player(base_dir):
        player = []
        guest_name_file = join(base_dir, "Name_Guest.txt")
        with open(guest_name_file, "r") as file:
            guest_name = file.readlines()[0]
            player.append(guest_name)

        home_name_file = join(base_dir, "Name_Home.txt")
        with open(home_name_file, "r") as file:
            home_name = file.readlines()[0]
            player.append(home_name)
        return player


