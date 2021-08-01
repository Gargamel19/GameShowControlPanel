from app.Models.Round import Round


class QuestionRound(Round):

    question = ""
    content = []
    correct = -1

    def __init__(self, question, content, correct):
        self.question = question
        self.content = content
        self.correct = correct
