import random

from brain_games.engine import engine


INSTRUCTION = '''What is the result of the expression?'''
MATH_SIGN = ('+', '-', '*', '/')


def check_answer(text: str):
    num1, sign, num2 = text.split()
    print(num1, sign, num2)
    return eval(f'{num1} {sign} {num2}')



def get_question() -> str:
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    return f'{num1} {random.choice(MATH_SIGN)} {num2}'

def game_calc():
    engine(INSTRUCTION, check_answer, get_question)

