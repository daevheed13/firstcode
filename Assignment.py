# Assignment 1
# filename = 'twist.txt'
# mode = 'r' #read only mode
# data = open(filename, mode)

# import random
# random_word = random.choice(data.read().split()).strip() #split the words and strip the spaces

# length = len(random_word)
# first_letter, second_letter, last_letter = random_word[0], random_word[1], random_word[-1]

# intro = input('\nWelcome to Hangman, press enter to continue : ')
# print(f"\nYour word has been chosen. Length = {length}, 1st letter = {first_letter}, 2nd letter = {second_letter} and last letter = {last_letter} ")
# answer = input('Enter the word : ')
# if answer == random_word:
#     print('\nAwesome!!! You\'re correct!')
# else:
#     print('\nSorry, you\'re wrong. The correct word is', random_word)

# Assignment 2
# import random

# number1, number2 = random.randint(1, 6), random.randint(1, 6)
# number3, number4 = random.randint(1, 6), random.randint(1, 6)
# number5, number6 = random.randint(1, 6), random.randint(1, 6)
# number7, number8 = random.randint(1, 6), random.randint(1, 6)
# number9, number10 = random.randint(1, 6), random.randint(1, 6)

# print('\nThis is a Dice-Roll Game. You\'ve only 5 tries \n')

# input('Press enter to roll the dice : ') #1st try
# if number1 == 6 and number2 == 6:
#     print(f'Osheyyyyy, you rolled {number1} & {number2}')
#     print('You Won!!!')
# else:
#     print(f'Sorry o, you rolled {number1} & {number2}')
#     print('4 tries remaining \n')

#     input('Press enter to roll the dice : ') #2nd try
#     if number3 == 6 and number4 == 6:
#         print(f'Osheyyyyy, you rolled {number3} & {number4}')
#         print('You Won!!!')
#     else:
#         print(f'Sorry o, you rolled {number3} & {number4}')
#         print('3 tries remaining \n')

#         input('Press enter to roll the dice : ') #3rd try
#         if number5 == 6 and number6 == 6:
#             print(f'Osheyyyyy, you rolled {number5} & {number6}')
#             print('You Won!!!')
#         else:
#             print(f'Sorry o, you rolled {number5} & {number6}')
#             print('2 tries remaining \n')

#             input('Press enter to roll the dice : ') #4th try
#             if number7 == 6 and number8 == 6:
#                 print(f'Osheyyyyy, you rolled {number7} & {number8}')
#                 print('You Won!!!')
#             else:
#                 print(f'Sorry o, you rolled {number7} & {number8}')
#                 print('1 try remaining \n')

#                 input('Press enter to roll the dice : ') #5th try
#                 if number9 == 6 and number10 == 6:
#                     print(f'Osheyyyyy, you rolled {number9} & {number10}')
#                     print('You Won!!!')
#                 else:
#                     print(f'Eiyaaaa, you rolled {number9} & {number10}')
#                     print('Game Over')

# import random

# input('Press enter to role the dice') #easier way
# for i in range(5):
#     die_1 = random.randint(1, 6)
#     die_2 = random.randint(1, 6)
#     print(die_1, die_2)

#     if die_1 == die_2 and die_1 == 6:
#         print('Yaaay, you won!!!!!')
#         break
#     else:
#         print('Oooops, you lost')
#     input('Press enter to play again')

# Assignment 3
# print('\nLoan Amortization calculator\n')
# loan_amount = int(input('Please enter a loan amount : '))
# interest_rate = float(input('Please enter an interest rate eg 5, 10... : '))
# years = float(input('Please enter the number of year(s) : '))

# monthly_interest_rate = ((1 + (interest_rate / 100)) ** (1/12)) - 1 # compound interest
# no_of_payments = int(years * 12)
# monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -no_of_payments)

# print('Months'.center(5), 'Payment'.center(11), 'Interest'.center(11), 'Principal'.center(11), 'Balance'.center(11), '\n')

# total_interest = 0
# for i in range(no_of_payments + 1): # range(12) = 0-11

#     if i == 0:
#         print(str(i).center(5), '-'.center(11), '-'.center(11), '-'.center(11), str(loan_amount).center(11))
#     else:
#         interest = loan_amount * (monthly_interest_rate)
#         principal = (monthly_payment - interest)
#         principal = round(principal, 2)
#         loan_amount = loan_amount - principal
#         monthly_payment, interest, loan_amount = round(monthly_payment, 2), round(interest, 2), round(loan_amount, 2)
#         total_interest += interest
        

#         print(str(i).center(5),str(monthly_payment).center(11), str(interest).center(11), str(principal).center(11), str(loan_amount).center(11))

# print(round(total_interest, 2))

# Multiplication Table
# for i in range (1, 5):
#     for n in range (1, 12):
#         #print(f"{n} x {i} = {n * i}".center(12), end = ' ')
#         print(f"{n * i}", end = "\t") # prints multiple of numbers on a row
#     print("\n")

# Diagram question
# for i in range(3):
#     print('a b c') # 3 numbers multiplied by 3
# print('-----')
# print('c c c') # the answer will equal the last number in 3 places
# print("What is the value of a,b,c?")
# #Diagram answer
# for i in range(333):
#     if str(i *3) == str(i)[-1] * 3:
#         print(f"{str(i)[0]} {str(i)[1]} {str(i)[2]}, {i} * 3 = {i * 3}")

# import random

# for trials in range(1,6):
#     print("\nTrial", trials)
#     random_numbers = []
#     already_counted = []
    
#     for i in range(1000):
#         for i in range(20):
#             randomNumber = random.randint(1, 7)
#             random_numbers.append(randomNumber)


    # print(f"Numbers".center(8), "Occurrences".center(12), "Percentage".center(11))
    # for item in random_numbers:
    #     if item not in already_counted:
    #         occurrences = random_numbers.count(item)
    #         already_counted.append(item)
    #         percentage = round((occurrences/20000) * 100, 1)
    #         print(f"{str(item).center(82)} {str(occurrences).center(11)} {str(percentage).center(11)}%")

# import citylist
# import requests
# import time
# import datetime

# cities = citylist.citylist

# requested_city = input("Please enter city to check \n: ").lower()

# for city in cities:
#     if requested_city in city["name"].lower():
#         print(city["name"], city["country"])

# requested_country = input("Please enter country code \n: ").lower()

# for city in cities:
#     if requested_city

# ------- Assignment ------ #

# 1 #
import random
list_1 = []
list_2 = []
def randnums(n):

    for number in range(n):
        
        num_1, num_2 = random.randint(0,20), random.randint(0,20)
        list_1.append(num_1)
        list_2.append(num_2)

randnums(5)
print(f"Lists : {list_1} and {list_2}")

# 2 #
mean1 = []
mean2 = []
def mean_randnums(n):
    mean_1 = sum(list_1) / n
    mean_2 = sum(list_2) / n
    
    mean1.append(mean_1)
    mean2.append(mean_2)
    
    print(f"Mean : {mean1} and {mean2}")

mean_randnums(5)

# def var_randnums():  
#     mapped = list(map(lambda x:((x - sum(mean1)) ** 2), list_1)) # mean deviation squared (x-mean)^2
#     print(mapped)
#     # variance = sum(mapped) / (n - 1)
#     # print(variance)
# var_randnums()

# 3 #
def var_randnums(n):
    dev1 = []
    dev2 = []
    
    for i in list_1:
        dev_1 = round((i - sum(mean1)) ** 2, 2)
        dev1.append(dev_1)

    for j in list_2:
        dev_2 = round((j - sum(mean2)) ** 2, 2)
        dev2.append(dev_2)
    
    var_1 = sum(dev1) / (n - 1)
    var_2 = sum(dev2) / (n - 1)
    
    print(f"Variance : {round(var_1, 2)} and {round(var_2, 2)}")
var_randnums(5)