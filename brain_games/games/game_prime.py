import random

from brain_games.const import RANDOM_MAX_VALUE, RANDOM_MIN_VALUE
from brain_games.engine import engine

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_answer(question):
    if question <= 1:
        return "no"
    for i in range(2, int(question**0.5) + 1):
        if question % i == 0:
            return "no"
    return "yes"


def get_question():
    number_for_question = random.randint(RANDOM_MIN_VALUE, RANDOM_MAX_VALUE)
    return number_for_question


def start_game():
    engine(INSTRUCTION, check_answer, get_question)
