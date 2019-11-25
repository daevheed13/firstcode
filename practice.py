# word = input('Please enter a word: ') # 1st 2, mid 2, last 2
# mid_1 = int(len(word)) // 2 # floor division removes the float
# mid_2 = mid_1 + 2 # 2 is added cause slice will stop at <2 which is the letter we need.

# statement = f'{word[0:2]}{word[mid_1:mid_2]}{word[-2:]}'
# print(statement)

# word = 'Sweet Mum' #displays Sweet reversed
# print(word[-5::-1])

# word = input('Enter 2 words with a space in-between eg Big Man: \n')
# splitted_word = word.split(' ')
# reversed_word = splitted_word[0][-1::-1] # prints reverse of first word
# print(reversed_word)

# print('Formula: c^2 = a^2 + b^2') # solving for c
# values = input('Enter value of a and b with format a,b : ')
# a,b = values.split(',')
# a_b = (float(a) ** 2) + (float(b) ** 2)
# c = (a_b ** .5)
# print(c)

# print('Solving a Quadratic Equation')
# values = input('Enter values with format a,b,c : ')
# a,b,c = values.split(',')
# a,b,c = float(a), float(b), float(c)

# x1 = (-b + ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)
# x2 = (-b - (((b ** 2) - (4 * a * c)) ** .5)) / (2 * a)

# statement = f'The roots are {round(x1.real, 2)} and {round(x2.real, 2)}'
# print(statement)
