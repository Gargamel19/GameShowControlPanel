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
            file.writelines(json.dumps(show_json, indent=4, sort_keys=True))

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
        show = Show.read_from_json(questions_json)

        if len(show.games) == 0:
            return show, show.games[index], []
        else:
            if index >= len(show.games):
                index = len(show.games)-1
            game = show.games[index]
            rounds = []
            for temp_round in game.rounds:
                if type(temp_round) is QuestionRound:
                    rounds.append([temp_round.winner, temp_round.question, temp_round.content, temp_round.correct])
                else:
                    rounds.append([temp_round.winner])
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
        with open(guest_name_file, "r", encoding="utf-8") as file:
            guest_name = file.readlines()[0]
            player.append(guest_name)

        home_name_file = join(base_dir, "Name_Home.txt")
        with open(home_name_file, "r", encoding="utf-8") as file:
            home_name = file.readlines()[0]
            player.append(home_name)
        return player

    @staticmethod
    def write_to_dir_structure(base_dir, show):

        # write name home
        Werkzeuge.write_line_to_file(base_dir, "Name_Home.txt", show.player_home)

        # write name guest
        Werkzeuge.write_line_to_file(base_dir, "Name_Guest.txt", show.player_guest)

        # create Games dir
        games_dir = join(base_dir, "Games")
        if not os.path.isdir(games_dir):
            os.mkdir(games_dir)

        # create Score dir
        score_dir = join(base_dir, "Score")
        if not os.path.isdir(score_dir):
            os.mkdir(score_dir)

        score_home = show.bonus_player_home
        score_guest = show.bonus_player_guest

        for x in range(len(show.games)):
            # create "Game x" dir
            game_dir = join(games_dir, "Game " + str(x))
            if not os.path.isdir(game_dir):
                os.mkdir(game_dir)
            score_game_dir = join(score_dir, "Game " + str(x))
            if not os.path.isdir(score_game_dir):
                os.mkdir(score_game_dir)

            # title
            Werkzeuge.write_line_to_file(game_dir, "Title.txt", show.games[x].title)

            # description
            Werkzeuge.write_lines_to_file(game_dir, "Description.txt", show.games[x].description)

            # rules
            Werkzeuge.write_lines_to_file(game_dir, "Rules.txt", show.games[x].rules)

            # Compute Score
            if show.games[x].winner == 0:
                score_home += x+1
            elif show.games[x].winner == 1:
                score_guest += x+1

            # Compute Round Score
            round_score_home = 0
            round_score_home_str = ""
            round_score_guest = 0
            round_score_guest_str = ""
            for temp_round in show.games[x].rounds:
                if temp_round.winner == 0:
                    round_score_home += 1
                    round_score_home_str += ") "
                    round_score_guest_str += "( "
                elif temp_round.winner == 1:
                    round_score_guest += 1
                    round_score_home_str += "( "
                    round_score_guest_str += ") "
                else:
                    round_score_home_str += "! "
                    round_score_guest_str += "! "

            Werkzeuge.write_line_to_file(score_game_dir, "Points.txt", str(round_score_home) + " : " +
                                         str(round_score_guest))
            Werkzeuge.write_line_to_file(score_game_dir, "Points_Home.txt", str(round_score_home))
            Werkzeuge.write_line_to_file(score_game_dir, "Points_Guest.txt", str(round_score_guest))

            Werkzeuge.write_line_to_file(score_game_dir, "Points_Home_Display.txt", str(round_score_home_str))
            Werkzeuge.write_line_to_file(score_game_dir, "Points_Guest_Display.txt", str(round_score_guest_str))

            if round_score_home > round_score_guest:
                Werkzeuge.write_line_to_file(score_game_dir, "Winner.txt", show.player_home)
            elif round_score_home < round_score_guest:
                Werkzeuge.write_line_to_file(score_game_dir, "Winner.txt", show.player_guest)

        # score home player
        Werkzeuge.write_line_to_file(score_dir, "Score_Home.txt", str(score_home))

        # score guest player
        Werkzeuge.write_line_to_file(score_dir, "Score_Guest.txt", str(score_guest))

    @staticmethod
    def write_line_to_file(directory, file, content):
        file_path = join(directory, file)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def write_lines_to_file(directory, file, content):
        file_path = join(directory, file)
        with open(file_path, 'w', encoding="utf-8") as f:
            f.writelines(content)
