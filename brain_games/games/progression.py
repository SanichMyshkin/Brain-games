from random import randint


CONDITION = 'Find the greatest common divisor of given numbers.'


def mass():
    start_point = randint(0, 30)
    step_interval = randint(0, 10)
    progres = [start_point, ]
    for i in range(0, 10):
        next_item = start_point + step_interval
        progres.append(next_item)
        start_point = next_item
    return progres


def question_and_answer():
    progression = mass()
    rand_index = randint(0, 9)
    correct_answer = progression[rand_index]
    progression[rand_index] = "??"
    qustion = " ".join(map(str, progression))
    return qustion, str(correct_answer)
