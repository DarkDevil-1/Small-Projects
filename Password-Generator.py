# password generator V2 is below generator V1
import random
import string


def error():
    print('You have entered an invalid value, TRY AGAIN')
    print('=' * 80, 'RESTART', '=' * 80)


def pass_gen_v1():
    symbols = '!@#$%^&*()'
    pandora_box = list(string.ascii_letters + string.digits)
    while True:
        try:
            length = int(input('Enter password length: '))
        except ValueError:
            error()
        else:
            break
    special_symbols = input('Do you need special symbols in your password (Y/N): ')

    if special_symbols == 'Y' or 'y':
        pandora_box += list(symbols)
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
    print(''.join(password), 'Is your generated password')
    # SUCCESS!!! Now we can run this function by running it


def pass_gen_v2():
    letter = list(string.ascii_letters)
    number = list(string.digits)
    symbols = list('!@#$%^&*()')
    pandora_box = list(string.ascii_letters + string.digits)

    while True:
        try:
            length = int(input('Enter password length: '))
        except ValueError:
            error()
        else:
            break

    choice = input('Do you want to include symbols in your password (Y/N): ')
    choice_2 = input('Do you wanna choose the specific amount of characters for each type (Y/N): ')
    yes = 'Y', 'y'
    no = 'N', 'n'
    if choice in yes and choice_2 in yes:
        while True:
            try:
                letter_count = int(input("Enter letter count in password: "))
                number_count = int(input("Enter number count in password: "))
                symbol_count = int(input("Enter symbol count in password: "))
                if letter_count < 0 or number_count < 0 or symbol_count < 0:
                    print('Enter a positive value')
                    pass_gen_v2()
            except ValueError:
                error()
            else:
                break

        pandora_count = letter_count + number_count + symbol_count
        if pandora_count > length:
            print("Total character count exceeds password length, TRY AGAIN")
            pass_gen_v2()

        else:
            password = []

            for i in range(letter_count):
                password.append(random.choice(letter))

            for i in range(number_count):
                password.append(random.choice(number))

            for i in range(symbol_count):
                password.append(random.choice(symbols))

            if pandora_count < length:
                random.shuffle(pandora_box)
                for i in range(length - pandora_count):
                    password.append(random.choice(pandora_box))

            random.shuffle(password)
            print('\n', ''.join(password), 'Is the generated password')

    elif choice in no and choice_2 in yes:
        while True:
            try:
                letter_count = int(input("Enter letter count in password: "))
                number_count = int(input("Enter number count in password: "))
                if letter_count < 0 or number_count < 0:
                    print('Enter a positive value')
                    pass_gen_v2()
            except ValueError:
                error()
            else:
                break
        pandora_count = letter_count + number_count
        if pandora_count > length:
            print('Total character count exceeds password length, TRY AGAIN')
            pass_gen_v2()

        else:
            password = []

            for i in range(letter_count):
                password.append(random.choice(letter))

            for i in range(number_count):
                password.append(random.choice(number))

            if pandora_count < length:
                random.shuffle(pandora_box)
                for i in range(length - pandora_count):
                    password.append(random.choice(pandora_box))

                    random.shuffle(password)
                    print('\n', ''.join(password), 'Is the generated password')

    elif choice in yes and choice_2 in no:
        pandora_box += list(symbols)
        random.shuffle(pandora_box)
        password = []
        for x in range(length):
            password.append(random.choice(pandora_box))
        random.shuffle(password)
        print('\n', ''.join(password), 'Is the generated password')
    else:
        random.shuffle(pandora_box)
        password = []
        for x in range(length):
            password.append(random.choice(pandora_box))
        random.shuffle(password)
        print('\n', ''.join(password), 'Is the generated password')


pass_gen_v2()
