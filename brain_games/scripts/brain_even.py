#!/usr/bin/env python3.
import random
import prompt

LOWER_LIMIT = 1
UPPER_LIMIT = 300


def main():
    logic()


def question_random_number():
    random_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)

    if check(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer


def check(random_number):
    return random_number % 2 == 0


def logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(DESCRIPTION)
    index = 0
    raund = 3

    while index < raund:
        question, correct_answer = question_random_number()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            return
        index = index + 1
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
