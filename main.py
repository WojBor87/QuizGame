from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(text=data["text"], answer=data["answer"]))

quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()

quiz.final_score()
