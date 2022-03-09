import random
import operator


CONDITION = 'What is the result of the expression?'


def get_question_and_answer():
    operand1 = random.randint(0, 99)
    operand2 = random.randint(0, 99)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    operation = random.choice(list(operations.keys()))

    answer = str(operations[operation](operand1, operand2))

    question = str(f"{operand1} {operation} {operand2}")

    return question, answer
