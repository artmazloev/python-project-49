import prompt

from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3
POSITIVE_FEEDBACK = "Correct!"


def start_game(INSTRUCTION, check_answer, get_question) -> None:
    engine(INSTRUCTION, check_answer, get_question)


def engine(instruction, check_function, data_for_question):
    name = welcome_user()
    print(instruction)
    for _ in range(NUMBER_OF_ROUNDS):
        question = data_for_question()
        print(f"Question: {question}")
        answer = prompt.string("Your answer:")
        correct_answer = check_function(question)
        if correct_answer == answer:
            print(POSITIVE_FEEDBACK)
        else:
            print(
                f""""{answer}" is wrong answer ;(. 
                Correct answer was "{correct_answer}". 
                Let's try again, {name}!"""
            )
            break
    else:
        print(f"Congratulations, {name}!")
