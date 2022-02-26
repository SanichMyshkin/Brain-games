#!/usr/bin/env python


from brain_games.engine import run_game  #импортируем функцию обработки
from brain_games.game import even        #импортируем функцию проверки на четность


def main():
    # старт
    run_game(even)


if __name__ == '__main__':
    main()
