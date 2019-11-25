# name = input('Enter your name: ')
# print(name[0],name[2],name[4],name[-1])
# print(name[0:5])

# word = input('Please input a word: ')
# length = input('What is the length of the word? ')
# int_len = int(int(length) / 2)
# print(word[int_len:])

# word = input('Please input a word: ')
# length = input('What is the length of the word? ')

# first_2 = word[0:2]
# last_2 = word[-2:]

# mid_a = int(int(length) / 2)
# mid_b = mid_a + 2
# mid_2 = word[mid_a:mid_b]

# statement = f"{first_2}{mid_2}{last_2}"
# print(statement)
# or 
# print(first_2+mid_2+last_2)

# word = 'Sweet Mum'
# slice = word[::2] #start from beg, stop at end and step 2 i.e it picks s,e,t,M,m = setMm
# print(slice)

# word = 'Sweet Mum'
# slice = word[::-1] #start from beginning, stop at end and step -1(reverse) i. reverse the whole word
# print(slice)

# word = 'Sweet Mum'
# slice = word[-5::-1] #start from t, stop at s and step -1(reverse)
# print(slice)

# print('Formula: c^2 = a^2 + b^2')
# a = input('What is the value of a? ')
# b = input('What is the value of b? ')

# int_a = (int(a) ** 2)
# int_b = (int(b) ** 2)

# c = (int_a + int_b) ** 0.5 #Squareroot


# print('The value of c is',c) 

# print('Solving a Quadratic Equation:')

# a = int(input('What is the value of a? '))
# b = int(input('What is the value of b? '))
# c = int(input('What is the value of c? '))

# x1_num = (-b) + ((b ** 2) - (4 * a * c)) ** 0.5
# x1_den = 2 * a
# x1 = x1_num / x1_den

# x2_num = (-b) - ((b ** 2) - (4 * a * c)) ** 0.5
# x2_den = 2 * a
# x2 = x2_num / x2_den

# statement = f'x is either {x1.real} or {x2.real}' # .real takes away the complex number
# print(statement)

# age = int(input('Please enter your age: '))

# can_drink = age >= 21
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40

# statement = f'Can drink: {can_drink}\nCan Pay Tax: {can_pay_tax}\nCan Take Pension: {can_take_pension}\nCan Retire: {can_retire}'

# print(statement)

# word = input('Enter a word: ')
# reversed_word = word[::-1]
# print(f'{word} is a palindrome: {word == reversed_word}')
# response = 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word
# print(f'{word} contains vowel(s): {response}')

# word = input('Please enter a word: ')
# print('a' in word) #check if a is in the word

# a = int(input('Value of a: '))
# b = int(input('Value of b: '))
# c = int(input('Value of c: '))
# d = int(input('Value of d: '))

# num = (a * d) + (c * b)
# den = (b * d)

# statement = f'{num} / {den}'
# print(statement)

# question = input('Enter a problem e.g "a/b+c/d" : ')
# splitted_question = question.split('+') #removes the '+' and breaks the string into 2 strings (0 & 1)
# frac1 = splitted_question[0]
# frac2 = splitted_question[1]

# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')

# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# question = input('Enter a problem e.g "a/b+c/d" : ') #easier method
# frac1, frac2 =  question.split('+') 
# a,b,c,d = *frac1.split('/'), *frac2.split('/')
# print(a,b,c,d)

# num = (int(a) * int(d)) + (int(c) * int(b))
# den = int(b) * int(d)

# statement = f'{num} / {den}'
# print(statement)

# dob = input('Please enter your date of birth with format "2019-10-20" : ')
# year = dob.split('-')[0] #removes the '-' from all places
# print(year)

# word = input('Please enter a word: ')
# print('a' in word)

# print(1,2,3,sep = '\n')
# print('new line')

# file = open('My_Data.csv', 'w') #writes codes inside excel file
# print('Name','Age','State','Due', file = file, sep = ',')
# print('Ade',20,'Ogun_State',20000, file = file, sep = ',')

# details = input('Enter details ie - "name, age, state, due" : ')
# name, age, state, due = details.split(',') 
# file = open('My_Data.csv', 'a')
# print(name,age,state,due, file = file, sep = ',')

# word = input('Plese enter a word; ')
# length = len(word)
# print(length)

# filename = 'lyrics.txt'
# mode = 'r' #read only mode
# data = open(filename, mode)

# lyrics = data.read()
# print(lyrics)

# my_range = range(20)
# print(type(my_range)) # Shows class of the object
# print(list(my_range)) # displays the set of numbers between 0 and 20

# my_range = range(20,60) # displays range. start:20, End:59
# my_range = range(20,60,2) # displays range. start:20, End:59, Step:2
# print(list(my_range))
# print(list(reversed(my_range))) # displays range reversed

# x = [1,2,5,3,10,1,0,4]
# print(sorted(x)) # sorts the values from lowest to greatest
# print(sorted(x, reverse = True)) # sorts the values from greatest to lowest
# x = list('Abimbolami') 
# print(sorted(x)) # list the characters alphabetically but Capital comes first

# my_list = ['seed', 'bee', 'a', 'checked', 'print']
# print(sorted(my_list)) # sorts alphabetically
# print(sorted(my_list, key = len)) # key tells it what you want to sort by. len sorts by the length from lowest
# print(sorted(my_list, key = len, reverse = True)) # reverses it

# x = [1,2,5,3,10,1,0,4]
# print(sum(x)) # sums all the values

# my_dict = dict(a = 20, b = 30)
# print(my_dict) # assigns values to a dictionary
# print(my_dict['a']) # displays value of 'a' 

# name = 'Abimbola'
# print(set(name)) # prints unique values

# nums = [1,2,3,4,5]
# mapped = map(lambda x:x*2, nums) # multiplies the values by 2
# print(list(mapped))

# names = ['ade', 'john', 'shola'] # map(function, iterable)
# mapped = map(lambda x:'Mr '+x, names) # adds 'Mr ' to the names
# print(list(mapped))

# word = 'Sharp'
# print(word.lower()) # prints word in lowercase

# word = input('Please enter the word you want to check: ')
# lower_word = word.lower() # lower() is a string method
# statement = 'a' in lower_word or 'e' in lower_word or 'i' in lower_word or 'o' in lower_word or 'u' in lower_word
# print(statement)

# word = input('Enter a word that starts with "Pre" : ')
# replaced_word = word.replace('Pre', 'Post') # replaces words
# print(replaced_word)

# names = ['gem', 'hem', 'blem', 'chem']
# mapped = map(lambda x:x.replace('e', 'a'), names) #replaces 'e' with 'a'
# print(list(mapped))

# lists = [1,3,1,2,2,4]
# mean = sum(lists) / len(lists) # mean
# mapped = list(map(lambda x:((x-mean) **2), lists)) # mean deviation squared (x-mean)^2
# print(mapped)
# variance = sum(mapped) / (len(lists) - 1)
# print(variance)

# a = 'Hello World'
# split_a = a.split(' ')
# join_a = ' '.join(split_a) # Joins words back. You need to define the delimiter again - ''.join
# print(join_a)

# filename = 'lyrics2.txt'
# mode = 'r' #read only mode
# data = open(filename, mode)

# lyrics = data.read()
# print(lyrics.find('Lupita')) # .find() - used to find position of words
# print(lyrics.count('skin')) # .count() - used to count the number of times a word appears
# .capitalize() - used to capitalize

#assignment 1
names = ['Bola', 'Shola', 'Segun', 'John']
mr = names[0], names[2], names[-1]
mrs = names[1]
mapped_mr = map(lambda x:'Mr '+x, mr)
mapped_mrs = map(lambda x:'Mrs '+x, mrs)
print(list(mapped_mr), *mapped_mrs)

#assignment 2
candy = int(input('Enter the number of candy you wish to share equally: '))
Equal_candy = candy // 3
crushed_candy = candy % 3
statement = f'Each friend will take {Equal_candy} and {crushed_candy} will be crushed'
print(statement)