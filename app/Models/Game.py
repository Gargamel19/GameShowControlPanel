from app.Models.Round import Round


class Game:

    title = ""
    description = []
    rules = []
    countdown_enabled = False
    countdown = 0
    stopwatch_enabled = False
    current_round = 0
    rounds = []
    scoreHome = 0
    scoreGuest = 0
    winner = -1

    def __init__(self, title, description, rules, countdown, stopwatch, current_round, rounds, scoreHome, scoreGuest, winner):
        self.winner = winner
        self.scoreHome = scoreHome
        self.scoreGuest = scoreGuest
        self.current_round = current_round
        self.rounds = rounds
        self.stopwatch_enabled = stopwatch
        self.countdown_enabled = countdown >= 0
        self.countdown = countdown
        self.rules = rules
        self.description = description
        self.title = title

    @staticmethod
    def readFromJson(json):
        title = json["Title"]
        desc = json["Description"]
        rules = json["Rules"]
        coutdown = json["Countdown"]
        stopwatch = json["Stopwatch"]
        current_round = json["CurrentRound"]
        rounds_json = json["Rounds"]
        if "Questions" in json:
            questions_json = json["Questions"]
        else:
            questions_json = []
        rounds = []
        for x in range(len(rounds_json)):
            if len(questions_json) > x:
                round = Round.readFromJson2(rounds_json[x], questions_json[x])
            else:
                round = Round.readFromJson1(rounds_json[x])
            rounds.append(round)
        scoreHome = json["ScoreHome"]
        scoreGuest = json["ScoreGuest"]
        winner = json["winner"]
        return Game(title, desc, rules, coutdown, stopwatch, current_round, rounds, scoreHome, scoreGuest, winner)
