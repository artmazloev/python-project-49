import random
import math


def check_answer(text: str):
    num1, num2 = int(text.split()[0]), int(text.split()[1])
    return math.gcd(num1, num2)



def get_question() -> str:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return f'{num1} {num2}'

def game_gcd() -> None:
    engine(INSTRUCTION, check_answer, get_question)

print(check_answer(get_question()))