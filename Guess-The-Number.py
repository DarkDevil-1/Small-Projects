import random

attempts_l = []


def score():
    if len(attempts_l) == 0:
        print('You have no attempts yet\n')
    else:
        print(f'\nYour highest score is {min(attempts_l)} attempts\n')


def game():
    rng = random.randint(1, 20)
    print('Welcome to the number guessing game!, Guess a number between 1 and 20')
    name = input('Enter your name: ')
    print(f'Hello {name}, Good luck on guessing the number!, You have 10 tries\n')
    score()
    attempts = 0

    while attempts < 10:
        try:
            guess = int(input('Enter your guess: '))
            if guess < 1 or guess > 20:
                print('Please enter a number between 1 and 20')
                continue
            elif guess == rng:
                print('You guessed the number!')
                attempts += 1
                attempts_l.append(attempts)
                score()
                y = input('Do you want to try again? (Y/N): ')
                if y == 'Y':
                    attempts = 0
                    print('You have 10 tries again, Good Luck!\n')
                    continue
                else:
                    print(f'Thanks for playing!, {name}, Your highest score was {min(attempts_l)} attempts')
                    break
            elif guess > rng:
                print('Your guess is higher\n')
                attempts += 1
                continue
            elif guess < rng:
                print('Your guess is lower\n')
                attempts += 1
                continue

        except ValueError:
            print('Please enter a valid number')
            continue

    else:
        print(f'You have exceeded the maximum number of tries, the number was {rng}')
        print(f'Thanks for playing!, {name}, Your highest score was {min(attempts_l)} attempts')


game()
