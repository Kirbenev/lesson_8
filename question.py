class Question:
    """
    Класс вопросов. Содержит в себе вопрос, сложность, ответ, ответ пользователя и количестов начисляемых
    за правильный ответ очков. А также методы для обработки вопросов.
    """

    def __init__(self, question, difficulty, answer, user_answer=None):
        self.question = question
        self.difficulty = int(difficulty)
        self.answer = answer
        self.user_answer = user_answer
        self.points = self.difficulty*10
        points = 0

    def __repr__(self):
        return f'{self.question} {self.difficulty} {self.answer} {self.user_answer} {self.points}'

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.user_answer == self.answer

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question}?\nСложность {self.difficulty}/5'

    def build_positive_feedback(self):

        """
        Возвращает:
        Ответ верный, получено __ баллов
        """
        return f"Ответ верный, получено {self.points} баллов\n"

    def build_negative_feedback(self):
        """Возвращает :
                 Ответ неверный, верный ответ __
                 """
        return f"Ответ неверный, верный ответ {self.answer}\n"

