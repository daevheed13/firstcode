# Assignment 1
filename = 'twist.txt'
mode = 'r' #read only mode
data = open(filename, mode)

import random
random_word = random.choice(data.read().split()).strip() #split the words and strip the spaces

length = len(random_word)
first_letter, second_letter, last_letter = random_word[0], random_word[1], random_word[-1]

intro = input('\nWelcome to Hangman, press enter to continue : ')
print(f"\nYour word has been chosen. Length = {length}, 1st letter = {first_letter}, 2nd letter = {second_letter} and last letter = {last_letter} ")
answer = input('Enter the word : ')
if answer == random_word:
    print('\nAwesome!!! You\'re correct!')
else:
    print('\nSorry, you\'re wrong. The correct word is', random_word)

# Assignment 2
import random

number1, number2 = random.randint(1, 6), random.randint(1, 6)
number3, number4 = random.randint(1, 6), random.randint(1, 6)
number5, number6 = random.randint(1, 6), random.randint(1, 6)
number7, number8 = random.randint(1, 6), random.randint(1, 6)
number9, number10 = random.randint(1, 6), random.randint(1, 6)

print('\nThis is a Dice-Roll Game. You\'ve only 5 tries \n')

input('Press enter to roll the dice : ') #1st try
if number1 == 6 and number2 == 6:
    print(f'Osheyyyyy, you rolled {number1} & {number2}')
    print('You Won!!!')
else:
    print(f'Sorry o, you rolled {number1} & {number2}')
    print('4 tries remaining \n')

    input('Press enter to roll the dice : ') #2nd try
    if number3 == 6 and number4 == 6:
        print(f'Osheyyyyy, you rolled {number3} & {number4}')
        print('You Won!!!')
    else:
        print(f'Sorry o, you rolled {number3} & {number4}')
        print('3 tries remaining \n')

        input('Press enter to roll the dice : ') #3rd try
        if number5 == 6 and number6 == 6:
            print(f'Osheyyyyy, you rolled {number5} & {number6}')
            print('You Won!!!')
        else:
            print(f'Sorry o, you rolled {number5} & {number6}')
            print('2 tries remaining \n')

            input('Press enter to roll the dice : ') #4th try
            if number7 == 6 and number8 == 6:
                print(f'Osheyyyyy, you rolled {number7} & {number8}')
                print('You Won!!!')
            else:
                print(f'Sorry o, you rolled {number7} & {number8}')
                print('1 try remaining \n')

                input('Press enter to roll the dice : ') #5th try
                if number9 == 6 and number10 == 6:
                    print(f'Osheyyyyy, you rolled {number9} & {number10}')
                    print('You Won!!!')
                else:
                    print(f'Eiyaaaa, you rolled {number9} & {number10}')
                    print('Game Over')

# Assignment 3
print('\nLoan Amortization calculator\n')
loan = float(input('Please enter a loan amount : '))
interest_rate = float(input('Please enter an interest rate eg 5, 10... : '))
years = float(input('Please enter the number of year(s) : '))

monthly_interest_rate = interest_rate / 1200
total_months = years * 12
monthly_payment = (loan * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_months)

statement = f'Your monthly payment is {round(monthly_payment, 2)}'
print(statement)