import random

letters = 'a A b B c C d D e E f F g G h H i I j J k K l M n N o O p Q r R s S t T u U v V w W x X y Y z Z'.split()

numbers = '1 2 3 4 5 6 7 8 9'.split()

symbols = '! @ # $ % ^ & * ( ) _ +'.split()

password_list = []
password_list2 = []
password = ''

number_of_letters = int(input("Enter number of letters :\n"))
number_of_numbers = int(input("Enter number of numbers:\n"))
number_of_symbols = int(input("Enter number of symbols:\n"))

for n in  range(0,number_of_letters):
    password_list.append(random.choice(letters))

for n in range(0,number_of_numbers):
    password_list.append(random.choice(numbers))

for n in range(0,number_of_symbols):
    password_list.append(random.choice(symbols))


for i in range (0,len(password_list)):
    x = random.randint(0,(len(password_list)))
    password_list2.insert(x,password_list[i])

for i in password_list2:
    password+=i
    

print(password)



