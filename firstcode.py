
num = 22
dem = 7
pi = num/dem
print(pi)
rounded_num = round(pi,2)
print(rounded_num)
phone = 9054833916 * 6
print(phone)

name = "Segun"
surname = "Ajikobi"
fullname = name+" "+surname
print(fullname)

day = '03'
month = ' June,'
year = ' 2019'
print(day+month+year)

pi = 22/7
statement = 'pi is ' + str(round(pi,2))
print(statement)

akara_price = 20
akamu_price = 50
akara = input('please how many akara do you want? ')
akamu = input('please how many akamu do you want? ')
akara_statement = 'you bought '+akara +' akara'
akamu_statement = 'and '+akamu+' akamu'
print(akara_statement, akamu_statement)

bill_akara = akara_price * int(akara)
bill_akamu = akamu_price * int(akamu)
total = bill_akara + bill_akamu
print('Your bill is',total)

name = input('Please enter your name: ')
age = input('Please enter your age: ')
current_year = 2019
year_born = current_year - int(age)
comment = f"hello {name}, you are {age}. You were born in {year_born}"
print(comment)

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))