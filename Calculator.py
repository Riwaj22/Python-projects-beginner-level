

import os

def addition():
    os.system('cls' if os.name == 'nt' else clear)
    print('Addition')

    continue_calc = 'y'

    num1 = float(input('Enter a Number:'))
    num2 = float(input('Enter another number:'))
    ans = num1+num2
    values_entered = 2
    print(f'Current Result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n):'))
        while continue_calc.lower() not in ['y','n']:
            print('Please enter y or n')
            continue_calc = (input('Enter more (y/n:'))

            if continue_calc.lower() == 'n':
                break
            num = float( input('Enter another number:'))
            ans = ans+num
            print(f'Current result: {ans}')
            values_entered += 1
    return [ans,values_entered]


def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num1 = float(input('Enter a Number:'))
    num2 = float(input('Enter another number:'))
    ans = num1-num2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter y or n')
            continue_calc = (input('Enter more (y/n:'))

            if continue_calc.lower() == 'n':
                break
            num = float(input('Enter another number:'))
            ans = ans - num
            print(f'Current result: {ans}')
            values_entered += 1
    return [ans, values_entered]


def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num1 = float(input('Enter a Number:'))
    num2 = float(input('Enter another number:'))
    ans = num1*num2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter y or n')
            continue_calc = (input('Enter more (y/n:'))

            if continue_calc.lower() == 'n':
                break
            num = float(input('Enter another number:'))
            ans = ans * num
            print(f'Current result: {ans}')
            values_entered += 1
    return [ans, values_entered]


def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num1 = float(input('Enter a Number:'))
    num2 = float(input('Enter another number:'))
    ans = num1 / num2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter y or n')
            continue_calc = (input('Enter more (y/n:'))

            if continue_calc.lower() == 'n':
                break
            num = float(input('Enter another number:'))
            ans = ans / num
            print(f'Current result: {ans}')
            values_entered += 1
    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        results = []
        print('Simple Calculator in Python')
        print('Enter a for addition')
        print('Enter s for subtraction')
        print('Enter m for multiplication')
        print('Enter d for division')
        print('Enter q for quit')

        choice = input('Selection: ')

        if choice == 'q':
            quit = True
            continue

        if choice == 'a':
            results = addition()
            print('Ans =',results[0],' total inputs: ',results[1])

        elif choice == 's':
            results = subtraction()
            print('Ans =', results[0], ' total inputs: ', results[1])

        elif choice == 'm':
            results = multiplication()
            print('Ans =', results[0], ' total inputs: ', results[1])

        elif choice == 'd':
            results = division()
            print('Ans =', results[0], ' total inputs: ', results[1])


        else:
            print('Invalid choice')


if __name__ == '__main__':
   calculator()







