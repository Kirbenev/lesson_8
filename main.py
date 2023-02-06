# импортируем необходимые функции
from funcs import get_questions, asking_questions, count_correct_answers

# получаем список объектов класса Question
questions = get_questions("package.json")

# Приветствуем пользователя и сообщаем о начале игры
print("Привет!\nИгра начинается\n")

# Запускаем цикл по спику и задаем вопросы пользователю
for question in questions:
    asking_questions(question)

# Считаем правильные ответы и выводим статистику
count_correct_answers(questions)