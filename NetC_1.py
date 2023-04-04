# # # my_name = 'Jarvis'


# # # print('Hello, my name is' + my_name + ', what is your name?')

# # # whatisyourname = input('What is your name\n')

# # print('Hello,' + whatisyourname + ', it is nice to meet you')

# # wizard = 'Harry'

# # print(f'You\'re a wizard,{wizard}')

# # yourhouse = input('What house are you in?\n' + 'Gryffindor,\n Slytherin,\n Ravenclaw,\n or Hufflepuff?\n')

# # print(f'Welcome to the Leaky Cauldron, {wizard} of house {yourhouse}.')


# name = 'Colden'

# age = 32

# actual_age = 32.3

# math = 5 ** 7 + 6 / 9 * 6 - 4

# results = math + actual_age + age

# print(results)

# hello this is a course that i am doing online, the online course is done by NetworkChuck!


print('Hello, Welcome to NetworkChuck Coffee!!!!!!!')

name = input('What is your name?\n')


if name == 'Ben' or name== 'Patricia' or name =='Loki':
    evil_status = input('Are you evil?\n')
    if evil_status == 'Yes':
       good_deeds = int(input('how many good deeds have you done?\n'))
       if good_deeds < 4:
           print(f'Get out {name}!')
           exit()
       else:
           print(print(f'Welcome to NetworkChuck Coffee {name}!'))
    else:
        print(f'Welcome to NetworkChuck Coffee {name}!')
        
        
else:
    print(f'Hello, {name}, thank you so much for coming in today. \n\n\n\n')

 # Coffee menu


beard_length = float(input('How long is your beard? in inches\n'))


if beard_length >= 1:
    print('Please move to the front of the line.')
else:
    print('Please move to the back of the line.')

menu = ('Black Coffee, Espresso, Latte, Cappucino, Frapuccino')


# # ask customer what they would like to order
print(name + ' what would you like from our menu today? here is what we are serving.  \n' + menu)


order = input()
count_of_order = int(input(f'How many {order} would you like?\n'))
if order == 'Frapuccino':
    price = 13.00 * count_of_order
    print(f'Your total is ${price}')
elif order == 'Cappucino':
    price = 10.00 * count_of_order
    print(f'Your total is ${price}')
elif order == 'Espresso':
    price = 5.00 * count_of_order
    print(f'Your total is ${price}')
elif order == 'Black Coffee':
    price = 3.00 * count_of_order
    print(f'Your total is ${price}')
if order == 'Latte':
    whip_cream = input('Would you like whip cream on your latte?\n')
    if whip_cream == 'Yes':
        price = 8.00 * count_of_order
        print(f'Your total is ${price}')
    else:
        price = 7.00 * count_of_order
        print(f'Your total is ${price}')
else:
    print('Sorry, we do not have that item on our menu.')

 

    print(f'Your total is ${price}')

# # how long the cout of order will take to make
time = (count_of_order) * 2


if count_of_order > 1:
    print(f'Your order of {count_of_order} {order}s will be ready in {time} minutes.')
else:
    print(f'Your order of {count_of_order} {order} will be ready in {time} minutes.')






















