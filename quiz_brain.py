class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
