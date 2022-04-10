class Round:
    winner = -1

    def __init__(self, winner):
        self.winner = winner

    @staticmethod
    def read_from_json2(json, question_round_json):
        from app.Models.QuestionRound import QuestionRound
        question_round_obs = QuestionRound(question_round_json["question"], question_round_json["content"],
                                           question_round_json["correct"])
        question_round_obs.winner = json["winner"]
        return question_round_obs

    @staticmethod
    def read_from_json1(json):
        return Round(json["winner"])
