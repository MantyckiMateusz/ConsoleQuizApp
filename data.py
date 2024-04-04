from html import unescape
import requests
import json
from question_model import Question

def get_questions(number_of_questions):
    questions = []
    url = f"https://opentdb.com/api.php?amount={number_of_questions}&type=boolean"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for el in data['results']:
            questions.append(Question(unescape(el['question']), el['correct_answer']))
        return questions
    else:
        print('Error fetching question data!')