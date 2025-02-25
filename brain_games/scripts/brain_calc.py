from brain_games.engine import start_game
from brain_games.games.game_calc import INSTRUCTION, check_answer, get_question


def main():
    start_game(INSTRUCTION, check_answer, get_question)


if __name__ == "__main__":
    main()
