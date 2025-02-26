from random import randint

PROGRESSION_LENGTH = 10

INSTRUCTION = "What number is missing in the progression?"


def check_answer(question):
    progression = question.split()
    missing_index = progression.index("..")
    valid = [(i, int(x)) for i, x in enumerate(progression) if x != ".."]
    i0, v0 = valid[0]
    i1, v1 = valid[1]
    diff = (v1 - v0) // (i1 - i0)
    if missing_index == 0:
        correct_value = int(progression[1]) - diff
    else:
        correct_value = int(progression[missing_index - 1]) + diff
    return str(correct_value)


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
