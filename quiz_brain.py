class QuizBrain:
    def __init__(self, question_data):
        self.score = 0
        self.current_question = 1
        self.question_data = question_data

    def ask_question(self):
        current_question = self.question_data[self.current_question]
        answer = input(f'Q.{self.current_question}: {current_question.text} (True/False)?: ')
        self.check_answer(current_question, answer) 
        self.show_score()
        self.current_question += 1

    def has_next_question(self):
        return not self.current_question == len(self.question_data)
            
    def check_answer(self, question, answer):
        if question.answer.lower() == answer.lower():
            print(f'You got it right!\nThe correct answer was: {question.answer}')
            self.score += 1
        else:
            print(f'That\'s wrong.\nThe correct answer was: {question.answer}')
    
    def show_score(self):
        print(f'Your current score is: {self.score}/{self.current_question}.')