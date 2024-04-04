from data import get_questions
from quiz_brain import QuizBrain

number_of_questions = int(input("Welcome to the quiz game!\nHow many questions would you like to answer?: "))
question_list = get_questions(number_of_questions)

quiz_brain = QuizBrain(question_list)
while quiz_brain.has_next_question():
    quiz_brain.ask_question()
