from random import randint
from math import gcd


CONDITION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = randint(20, 99)
    num2 = randint(20, 99)
    answer = str(gcd(num1, num2))
    question = str(f"{num1} {num2}")
    return question, answer
