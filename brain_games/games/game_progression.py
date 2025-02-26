from random import randint

PROGRESSION_LENGTH = 10

INSTRUCTION = "What number is missing in the progression?"


def check_answer(question):
    progression = question.split()
    missing_index = progression.index("..")
    
    if missing_index == 0:
        diff = int(progression[2]) - int(progression[1])
        correct_value = str(int(progression[1]) - diff)
    else:
        diff = int(progression[missing_index + 1]) - int(
            progression[missing_index - 1])
        correct_value = str(int(progression[missing_index - 1]) + diff)
    
    return correct_value


def get_question():
    progression = []
    initial_value = randint(1, 100)
    step_value = randint(1, 5)

    for i in range(PROGRESSION_LENGTH):
        progression.append(str(initial_value + i * step_value))

    hidden_element_index = randint(0, PROGRESSION_LENGTH - 1)
    progression[hidden_element_index] = ".."
    question = " ".join(progression)
    return question
