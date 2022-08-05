import random

attempts_l = []


def score():
    if len(attempts_l) == 0:
        print('You have no attempts yet')
    else:
        print(f'The current high score is {min(attempts_l)} attempts')


def game():
    rng = random.randint(1, 20)
    print('Welcome to the number guessing game!, Guess a number between 1 and 20')
    name = input('Enter your name: ')
    print(f'Hello {name}, Good luck on guessing the number!\n')
    score()
    attempts = 0

