from random import randint


CONDITION = 'What is the result of the expression?'


def question_and_answer():
    num1 = randint(0, 99)
    num2 = randint(0, 99)
    symbol = randint(0, 2)
    if symbol == 0:
        result = num1 + num2
        qustion = str(f"{num1} + {num2}")
        return qustion, str(result)
    elif symbol == 1:
        result = num1 - num2
        qustion = str(f"{num1} - {num2}")
        return qustion, str(result)
    else:
        result = num1 * num2
        qustion = str(f"{num1} * {num2}")
        return qustion, str(result)
