import json
import os
from random import randrange

def read_question_from_file():
    file_path = os.path.join(os.path.dirname(__file__), "Question_list.json")
    with open(file_path, "r") as file:
        d = json.load(file)
        # print(d)
        return d 





data = read_question_from_file()



"""
    method to print the question
"""
def print_question(question_number):
    question = data[question_number]
    for key,value in question.items():
        print(f"ID: {key}")
        print(f"Question: {value['question']}")
        print(f"Options: {', '.join(value['options'])}")
   


"""
    method for genrating a random number between 1 to 10:
"""

"""
question engine
"""

def question_engine(question_number):
    question = data[question_number]

    for key, value in question.items():
        question_id = key
        display_question = value['question']
        option_list = value['options']
        correct_answer = value['answer']

        return {
            "id": question_id,
            "question": display_question,
            "options": option_list,
            "answer": correct_answer
        }
    