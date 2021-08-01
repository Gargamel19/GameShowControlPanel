

class Round:
    winner = -1

    def __init__(self, winner):
        self.winner = winner

    @staticmethod
    def readFromJson2(json, questionRound_json):
        from app.Models.QuestionRound import QuestionRound
        questionRoundObs = QuestionRound(questionRound_json["question"],
                                                       questionRound_json["content"],
                                                       questionRound_json["correct"])
        questionRoundObs.winner = json["winner"]
        return questionRoundObs

    @staticmethod
    def readFromJson1(json):
        return Round(json["winner"])
