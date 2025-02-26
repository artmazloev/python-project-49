import random

from brain_games.engine import engine

INSTRUCTION = (
    'Answer "yes" if the number is even, '
    'otherwise answer "no".'
)


def check_answer(n):
    return "yes" if n % 2 == 0 else "no"


def get_question():
    number_for_question = random.randint(0, 100)
    return number_for_question


def start_game():
    engine(INSTRUCTION, check_answer, get_question)
