import json
from question import Question

def get_questions(filename):

    """ Функция загружает список полей для Класса вопросы из JSON Файла  и возвращает список объктов класа Question"""
    questions = []
    with open(filename) as f:
        raw_json = f.read()
    q = json.loads(raw_json)

    for i in q:
        questions.append(Question(i['q'], i['d'], i['a'], ))
    return questions

def asking_questions(question):

    """ Задаем вопрос и проверяем корректность ответа пользователя"""
    print(question.build_question())
    question.user_answer = input()
    if question.is_correct():
        print(question.build_positive_feedback())
    else:
        print(question.build_negative_feedback())

def count_correct_answers(questions):
    """ Считает количетсво правильных ответов и полученных балов"""
    count = 0
    score = 0
    for question in questions:
        if question.answer == question.user_answer:
            count += 1
            score += question.points
    print(f'Отвечено {count} вопроса из {len(questions)}\n')
    print(f'Набранно {score} баллов')

