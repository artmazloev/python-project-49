from random import randint

PROGRESSION_LENGTH = 10

INSTRUCTION = "What number is missing in the progression?"


def check_answer(question):
    progression = question.split()
    if not (progression[0] == ".." or progression[1] == ".."):
        diff = int(progression[1]) - int(progression[0])
    else:
        diff = int(progression[3]) - int(progression[2])
    missing_value = progression.index("..")
    correct_value = str(int(progression[missing_value - 1]) + diff)
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
