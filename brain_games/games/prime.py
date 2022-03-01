from random import randint


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def question_and_answer():
    num = randint(2, 99)
    flag = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = 1
    if flag == 0:
        return str(num), "yes"
    else:
        return str(num), "no"
