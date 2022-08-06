import sys
import math


def error():
    print('You have entered an Invalid value. Please try the program again. Thank You')
    print('=' * 80, 'RESTART', '=' * 80)


def arithmetic_calc():
    while True:
        print(
            '***** FOR LOGARITHM, ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, SQUARE-ROOT, POWER, RADIAN, DEGREE, '
            'REMAINDER *****')
        print('OPERATORS = log , + , - , * , /, %, sqrt , ^, rad, deg')

        try:
            num1 = float(input('Number 1 here:'))
            op = input('Enter Operator:')
            operator = 'log', '+', '-', '^', '*', '/', 'sqrt', 'rad', 'deg'
            if op not in operator:
                print('Invalid Operator')
                sys.exit()
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
