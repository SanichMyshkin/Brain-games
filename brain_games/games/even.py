from random import randint

CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    num = randint(0, 99)
    qustion = str(num)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return qustion, correct_answer
