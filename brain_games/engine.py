import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game.CONDITION)
    game_rounds_count = 3
    for round_number in range(0, game_rounds_count):
        question, correct_answer = game.question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break
        print("Correct!")
<<<<<<< HEAD
=======
        count += 1
>>>>>>> 5b1248e48b48dc555e92e4611dd83c82f034ffbd
    else:
        print(f"Congratulations, {user_name}!")
