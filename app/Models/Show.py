from app.Models.Game import Game


class Show:
    player_home = ""
    player_guest = ""
    bonus_player_home = 0
    bonus_player_guest = 0

    games = []

    def __init__(self, player_home, player_guest, bonus_player_home, bonus_player_guest, games):
        self.player_home = player_home
        self.player_guest = player_guest
        self.bonus_player_guest = bonus_player_guest
        self.bonus_player_home = bonus_player_home
        self.games = games

    @staticmethod
    def read_from_json(json):
        player_home = json["player_home"]
        player_guest = json["player_guest"]
        bonus_player_home = json["bonus_player_home"]
        bonus_player_guest = json["bonus_player_guest"]
        games = []
        for game in json["games"]:
            games.append(Game.read_from_json(game))

        return Show(player_home, player_guest, bonus_player_home, bonus_player_guest, games)
