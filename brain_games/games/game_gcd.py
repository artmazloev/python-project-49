import math
import random

from brain_games.const import RANDOM_MAX_VALUE, RANDOM_MIN_VALUE
from brain_games.engine import engine

INSTRUCTION = """Find the greatest common divisor of given numbers."""


def check_answer(text: str) -> str:
    num1, num2 = int(text.split()[0]), int(text.split()[1])
    return str(math.gcd(num1, num2))


def get_question() -> str:
    num1, num2 = random.randint(
        RANDOM_MIN_VALUE, RANDOM_MAX_VALUE), random.randint(
        RANDOM_MIN_VALUE, RANDOM_MAX_VALUE
    )
    return f"{num1} {num2}"


def start_game() -> None:
    engine(INSTRUCTION, check_answer, get_question)
