import random

from brain_games.const import RANDOM_MAX_VALUE, RANDOM_MIN_VALUE
from brain_games.engine import engine

INSTRUCTION = """What is the result of the expression?"""
MATH_SIGN = ("+", "-", "*")


def check_answer(text: str):
    num1, sign, num2 = text.split()
    print(num1, sign, num2)
    return str(eval(f"{num1} {sign} {num2}"))


def get_question() -> str:
    num1, num2 = random.randint(
        RANDOM_MIN_VALUE, RANDOM_MAX_VALUE), random.randint(
        RANDOM_MIN_VALUE, RANDOM_MAX_VALUE
    )
    return f"{num1} {random.choice(MATH_SIGN)} {num2}"


def start_game():
    engine(INSTRUCTION, check_answer, get_question)
