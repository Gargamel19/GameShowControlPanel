from app.Models.Round import Round


class Game:

    title = ""
    description = ""
    rules = ""
    countdown_enabled = False
    countdown = 0
    current_round = 0
    rounds = []
    scoreHome = 0
    scoreGuest = 0
    winner = -1

    def __init__(self, title, description, rules, countdown, current_round, rounds, score_home, score_guest,
                 winner):
        self.winner = winner
        self.scoreHome = score_home
        self.scoreGuest = score_guest
        self.current_round = current_round
        self.rounds = rounds
        self.countdown_enabled = countdown >= 0
        self.countdown = countdown
        self.rules = rules
        self.description = description
        self.title = title

    @staticmethod
    def read_from_json(json):
        title = json["Title"]
        desc = json["Description"]
        rules = json["Rules"]
        countdown = json["Countdown"]
        current_round = json["CurrentRound"]
        rounds_json = json["Rounds"]
        if "Questions" in json:
            questions_json = json["Questions"]
        else:
            questions_json = []
        rounds = []
        for x in range(len(rounds_json)):
            if len(questions_json) > x:
                temp_round = Round.read_from_json2(rounds_json[x], questions_json[x])
            else:
                temp_round = Round.read_from_json1(rounds_json[x])
            rounds.append(temp_round)
        score_home = json["ScoreHome"]
        score_guest = json["ScoreGuest"]
        winner = json["winner"]
        return Game(title, desc, rules, countdown, current_round, rounds, score_home, score_guest, winner)
