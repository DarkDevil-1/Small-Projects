import random
import string


def error():
    print('You have entered an Invalid value, TRY AGAIN')
    print('=' * 80, 'RESTART', '=' * 80)


def pass_gen():
    symbols = '!@#$%^&*()'
    pandora_box = list(string.ascii_letters + string.digits)
    while True:
        try:
            length = int(input('Enter Password Length: '))
        except ValueError:
            error()
        else:
            break
    special_symbols = input('Do You Need Special Symbols In Your Password (Y/N): ')

    if special_symbols == 'Y' or 'y':
        pandora_box = list(string.ascii_letters + string.digits + symbols)
    else:
        pass

    # PASSWORD GENERATION PROCESS
    random.shuffle(pandora_box)
    password = []  # Characters are in a list so password must also be one to not raise an error
    for x in range(length):
        password.append(random.choice(pandora_box))
    # Shuffle
    random.shuffle(password)
    # Since we needa convert the password to string to make it presentable we do this,
    print('\n')
    print(''.join(password), 'Is Your Generated Password')
    # SUCCESS!!! Now we can run this function by running it


pass_gen()
