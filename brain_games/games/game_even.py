import random

from brain_games.engine import engine

INSTRUCTION = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_even(n):
    return "yes" if n % 2 == 0 else "no"


def get_question():
    number_for_question = random.randint(0, 100)
    return number_for_question


def game_even():
    engine(INSTRUCTION, is_even, get_question)

