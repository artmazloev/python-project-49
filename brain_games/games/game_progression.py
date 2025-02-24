from random import randint

from brain_games.engine import engine



PROGRESSION_LENGTH = 10

DESCRIPTION = 'What number is missing in the progression?'


def make_game_data(): 
    progression = []
    initial_value = randint(1, 100)
    step_value = randint(1, 100)

    for i in range(PROGRESSION_LENGTH):
        progression.append(str(initial_value + i * step_value))

    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)
    print(type(question), question)
    return (question, correct_answer)