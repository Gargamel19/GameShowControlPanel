from app.Models.Game import Game


class Show:
    playerHome = ""
    playerGuest = ""
    bonusPlayerHome = 0
    bonusPlayerGuest = 0

    games = []

    def __init__(self, playerHome, playerGuest, bonusPlayerHome, bonusPlayerGuest, games):
        self.playerHome = playerHome
        self.playerGuest = playerGuest
        self.bonusPlayerGuest = bonusPlayerGuest
        self.bonusPlayerHome = bonusPlayerHome
        self.games = games

    @staticmethod
    def readFromJson(json):
        playerHome = json["playerHome"]
        playerGuest = json["playerGuest"]
        bonusPlayerHome = json["bonusPlayerHome"]
        bonusPlayerGuest = json["bonusPlayerGuest"]
        games = []
        for game in json["games"]:
            games.append(Game.readFromJson(game))

        return Show(playerHome, playerGuest, bonusPlayerHome, bonusPlayerGuest, games)