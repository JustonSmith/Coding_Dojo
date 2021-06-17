# Syntax
    # code block: ie functions, conditionals, loops, classes * OOP
    # uses : and intentation

# Data Types/Structures: strings, numbers (floats(decimals), integers(whole), complex ie 3p), booleans, none 
    # data structures are collections of data types. 
    # use method (type)

num1 = 12
print (type(num1))
num2 = 24.5
print (type(num2))

my_str = "My num is"

print(my_str + str(num1))



# List [] 
    # lists are like arrays in JS.

my_list = [1, 2, 3]
my_list.append(4)
print (my_list[1])
print (type(my_list))

# Tuples () immutable list. will have parenthesis around it in terminal.

my_tuple = (1, 2, 3)
    # my_tuple[2] = 4
print('length is:', len(my_list))
for num in range(len(my_list)):
    print('index is', num)
    print('value is', my_list[num])
    print('-' *20)

# Dictionaries - key value {}

my_dict = {'name': 'Judge', 'location': 'Dallas'}
print (my_dict ['name'])
print (my_dict['location'])
my_dict['location'] = 'Seattle'
print (my_dict['location'])
print (my_dict)

for k, v in my_dict.items(): # .items method will give us key value pair combined together.
    print('key is', k)
    print('value is', v)

    """
    PSEUDOCODE: for INDEX ONE, INDEX TWO in DICTIONARY.ITEMS() - THIS WILL RETURN A TUPLE WITH A LENGTH OF 2, (KEY, VALUE) FOR EACH KEY:VALUE PAIR IN THE DICTIONARY.
    
    """


# Conditionals
if 1 < 2:
    print("its greater")
elif 1 == 2:
    print("It's equal")
else:
    print("its less")

# Loops : start, end, step(increment/decrement)
x = 0
while(x > 4):
    print('x is', x)
    x += 1 # ++ does not work in python
print('x at the end', x)

for x in range(0, 4, 2):
    print('x is, x')
print ('x at the end', x)






[] - initialize a list, or index(list, tuples)