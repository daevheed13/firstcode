# Learning if, else and ifelse statements

# if 'foo' in ['foo', 'bar', 'baz']:
#     print('Outer condition is true')

#     if 10 > 20:
#         print('Inner condition 1') # won't print because the expression is not true

#     print('Between inner conditions') # will print because it is under the first if but not under the second

#     if 10 < 20:
#         print('Inner condition 2') # will print because the expression is not true

#     print('End of outer condition')

# print('After outer condition') # this is not under the if statement

# x = 20
# if x < 50:
#     print('(first suite)')
#     print('x is small')
# else:
#     print('(second suite)')
#     print('x is large')

# behaviour = input('is your behaviour good or bad? ')
# age = int(input('What is your age? '))
# if (behaviour == 'good') and (age < 18):
#     print('You get a toy')
# if (behaviour == 'good') and (age > 18):
#     print('You get a car')
# if (behaviour == 'bad'):
#     print('Left alone')

# behaviour = input('is your behaviour good or bad? ')
# age = int(input('What is your age? '))
# if behaviour == 'good':
#     if age < 18:
#         print("Here's your toy!!!")
#     else:
#         print("Here's your car!!!")
# else:
#     print("You're on your own")

# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print('This wont happen')
# elif var:
#     print('This wont either')

# Tenary Expression - can be assigned to a variable and can print a statement
# score = int(input('What was your score? '))
# status = 'You Passed!!!' if score >= 50 else 'You Failed' # You Failed replaces You Passed if the expression is false
# print(status)

# x = y = 40
# z = 1 + x if x > y else y + 2 # x is not greater than y so the else statement runs
# print(z)

# x = y = 40
# z = 1 + (x if x > y else y) + 2 # 1 + y + 2 because the expression is false
# print(z)

# x = 43
# y = 40
# z = 1 + (x if x > y else y) + 2 # 1 + x + 2 because the expression is true
# print(z)

# x = 3
# s = ('foo' if (x == 1) else ('bar' if (x == 2) else ('baz' if (x == 3) else ('qux' if (x == 4) else 'quux'))))
# print(s)

que = input('Are you okay? true or false: ')
if que == 'false':
    que_1 = input('Do you have pains? ')
    
    if que_1 == 'true':
        que_2 = input('Did you sleep well? ')
        
        if que_2 == 'true':
            que_3 = input('Have you done hardwork? ')
            
            if que_3 == 'false':
                que_4 = input('Do you have a fever? ')
                
                if que_4 == 'true':
                    que_5 = input('Are you vomitting? ')
                    
                    if que_5 == 'true':
                        print('Please see a doctor')
                    else:
                        print('Take Some Anti-Malaria')
                else:
                    print('Inconclusive, please see a doctor')
            else:
                print('Have some pain killer')
        else:
            print('Try to sleep')
    else:
        print('Unable to diagnose now')
else:
    print('Please get a life')