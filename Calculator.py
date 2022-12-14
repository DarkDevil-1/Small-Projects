import math


def error():
    print('You have entered an Invalid value. Please try the program again. Thank You')
    print('=' * 80, 'RESTART', '=' * 80)


def arithmetic_calc():
    print(
        '***** FOR LOGARITHM, ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, SQUARE-ROOT, POWER, RADIAN, DEGREE, '
        'REMAINDER *****')
    print('OPERATORS = log , + , - , * , /, %, sqrt , ^, rad, deg')
    while True:
        try:
            num1 = float(input('Number 1 here:'))
            op = input('Enter Operator:')
            operator = 'log', '+', '-', '^', '*', '/', 'sqrt', 'rad', 'deg'
            if op not in operator:
                print('Invalid Operator')
                continue
            if op == 'log':
                log = math.log10(num1)
                print('Answer:', log)
            elif op == 'rad':
                rad = math.radians(num1)
                print(rad)
            elif op == 'deg':
                deg = math.degrees(num1)
                print(deg)
            elif op == 'sqrt':
                sqrt = math.sqrt(num1)
                print('Answer:', sqrt)
            else:
                num2 = float(input('Number 2 here:'))
                if op == '+':
                    print('Answer:', num1 + num2)
                elif op == '-':
                    print('Answer:', num1 - num2)
                elif op == '/':
                    print('Answer:', num1 / num2)
                elif op == '*':
                    print('Answer:', num1 * num2)
                elif op == '^':
                    power = math.pow(num1, num2)
                    print('Answer:', power)
                elif op == '%':
                    val = num1 % num2
                    print('Answer:', val)
        except ValueError:
            error()
        else:
            break


def quad():
    while True:
        try:
            print("************** QUADRATIC EQUATION ROOTS CALCULATOR **************")
            print('Of the form ax^2 + bx + c = 0')
            a = int(input('Enter value of A: '))
            b = int(input('Enter value of B: '))
            c = int(input('Enter value of C: '))
            if a == 0:
                print('THE VALUE OF A CANNOT BE 0, PLEASE TRY AGAIN')
            else:
                delta = b ** 2 - (4 * a * c)
                root1 = (-b + math.sqrt(delta)) / 2 * a
                root2 = (-b - math.sqrt(delta)) / 2 * a
                if delta == 0:
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [root1, root2])
                    print('The roots of this equation are real and equal')
                elif delta > 0:
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [root1, root2])
                    print('The roots of this equation are real and distinct')
                elif delta < 0:
                    root1 = (-b + (delta ** 0.5)) / 2 * a
                    root2 = (-b - (delta ** 0.5)) / 2 * a
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('IS =', [root1, root2])

                    print('\nThe roots are complex and imaginary')
            print('\nProgram Over')
        except ValueError:
            error()
        else:
            break


def factorial():
    while True:
        try:
            num = int(input('Enter Number:'))
            if num == 0:
                print('Factorial of 0 is 1')
            elif num < 0:
                print('Factorial does not exist for -ve numbers')
            else:
                fact = 1
                index = 1
                while index <= num:
                    fact *= index
                    index += 1
                print('The Factorial of', num, 'is', fact)
        except ValueError:
            error()
        else:
            break


def main():
    while True:
        print('\n1. Arithmetic Calculator')
        print('2. Quadratic Equation Calculator')
        print('3. Factorial Calculator')
        print('4. Exit\n')
        try:
            choice = int(input('Enter your choice:'))
            if choice == 1:
                arithmetic_calc()
            elif choice == 2:
                quad()
            elif choice == 3:
                factorial()
            elif choice == 4:
                print('\nThank You')
                break
            else:
                print('Invalid Choice\n')
        except ValueError:
            error()
        else:
            break
