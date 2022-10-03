from utils import load_question, build_statistic
import random

file_name = 'question.json'
questions = load_question(file_name)
random.shuffle(questions)

for i in questions:
    answer = input(i.build_question())
    i.user_answer = answer
    print(i.build_feedback())

print(build_statistic(questions))





