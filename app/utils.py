from os import listdir
from os.path import join


class Werkzeuge:

    @staticmethod
    def load_games(base_dir):
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
