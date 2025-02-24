import random

from brain_games.engine import engine

INSTRUCTION = """Answer 'yes' if given number is prime. Otherwise answer 'no'"""


def is_prime(n):
    if n <= 1:
        return 'no'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def get_question():
    number_for_question = random.randint(1, 100)
    return number_for_question


def game_prime():
    engine(INSTRUCTION, is_prime, get_question)

