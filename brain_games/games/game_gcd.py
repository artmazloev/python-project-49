import math
import random

from brain_games.engine import engine

INSTRUCTION = """Find the greatest common divisor of given numbers."""


def check_answer(text: str) -> str:
    num1, num2 = int(text.split()[0]), int(text.split()[1])
    return str(math.gcd(num1, num2))


def get_question() -> str:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return f"{num1} {num2}"


def start_game() -> None:
    engine(INSTRUCTION, check_answer, get_question)
