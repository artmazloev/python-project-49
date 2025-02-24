import prompt

from brain_games.cli import welcome_user


NUMBER_OF_ROUNDS = 3
POSITIVE_FEEDBACK = "Correct!"
NEGATIVE_FEEDBACK = "Wrong!"
CONGRATULATIONS = "Congratulations!"


def engine(instruction, check_function, data_for_question):
    welcome_user()
    print(instruction)
    for _ in range(NUMBER_OF_ROUNDS):
        question = data_for_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        if check_function(question) == answer:
            print(POSITIVE_FEEDBACK)
        else:
            print(NEGATIVE_FEEDBACK)
            break
    else:
        print(CONGRATULATIONS)