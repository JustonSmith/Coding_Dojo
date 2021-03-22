

# NOTES #



#_____STRINGS_____ #



# string literals #

print('this is a sample string')

# concatenation of strings and variables #

name = 'zen'
print('my name is', name) # use of comma

name = 'zen'
print('my name is' + name) # use of '+'

# string interpolation #

first_name = 'zen' 
last_name = 'coder'
age - 27
print(f"my name is {first_name} {last_name} and I am {age} years old.") # f string interpolation

first_name = 'zen'
last_name = 'coder'
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age)) # string.format interpolation

hw = "Hello %s" % "World"
py = "I love Python %d" % 3
print(hw, py) # % format with literals

name = 'zen'
age = 27
print("my name is %s and I'm %d" % (name, age)) # % format with variables

x = "hello world"
print(x.title()) # built in string method

# string.upper(): UPPERCASE

# string.lower(): lowercase

# string.count(substring): returns number of occourances in substring

# string.split(char): returns a list of values where string is split at the given character. Default is at every space.

# string.find(substring): returns the index of the strat of the first occourance of substring within string.

#string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.

# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.

# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.




#_____INDENTATION AND LINE ENDINGS_____#



# if statement is example of code block. IF statement gives the condition, but the line(s) that follow explain what we want to happen IF the condition is true. Code block KEYWORDS: def, if, elif, else, for, while, class.

x = 10
    if x > 50:
        print("bigger than 50")
    else:
        print("smaller than 50")

# Pass when you want to leave something empty.
class empty_class:
    pass

for val in my_string:
    pass



#______DATA TYPES_____#



# primitive data types include boolean, numbers, and strings.

# composite data types include tuples, lists, and dictionaries. 

# tuples are immutable and can contain mixed data types. EX:

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# lists are mutable and can hold a group of values. Usually meant to store a collection of related data. EX:

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# dictionaries are a group of key_value pairs. Dictionary elements are indexed by unique keys which are used to access values. EX:

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}



#_____COMMON FUNCTIONS_____#



# type used whenever you are unsure of the variables data type. EX:

print(type(2.63)                # output: <class 'float>
printcopy(type(new_person))     # output: <class 'dict'>

# len is used for data types with a length attribute such as lists, dictionaries, tuples, and strings. EX:

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11



#_____TYPE CASTING or EXPLICIT TYPE CONVERSION _____#


# We may find ourselves wanting to change a value's data type from one type to another. For example, in the Hello World assignment, trying to print a string plus a number resulted in a TypeError. Python doesn't know how to add a string and a number, but it can add two strings together, so if we can cast the number as a string, then we will be able to "add" the two values together, like so:

print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42



#_____CONDITIONALS_____#



# Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.  These statements control the flow our code is executed by the interpreter.  In Python, the keywords for conditional statements are if, elif, and else. Here are some examples:

x = 12
    if x > 50:
    print("bigger than 50")
    else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
    if x > 10:
    print("bigger than 10")
    elif x > 50:
    print("bigger than 50")
    else:
    print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    if x < 10:
    print("smaller than 10")
    # nothing happens, because the statement is false



#_____COMPARISON AND LOGIC OPERATORS_____#



# ==	
# Checks if the value of two operands are equal	1 == 2 => False
# 1 == 1 => True

# !=
# Checks if the value of two operands are not equal	1 != 2 => True
# 1 != 1 => False

# >
# Checks if the value of left operand is greater than the value of right operand	
# 1 > 2 => False
# 2 > 1 => True

# <	
# Checks if the value of left operand is less than the value of right operand	
# 1 < 2 => True
# 2 < 1 => False

# >=	
# Checks if the value of left operand is greater than or equal to the value of right operand	
# 1 >= 2 => False
# 2 >= 2 => True

# <=	
# Checks if the value of left operand is less than or equal to the value of right operand	
# 1 <= 2 => True
# 2 <= 2 => True

# and	
# Checks that each expression on the left and right are both True	
# (1 <= 2) and (2 <= 3) => True
# (1 <= 2) and (2 >= 3) => False
# (1 >= 2) and (2 >= 3) => False

# or	
# Checks if either the expression on the left or right is True	
# (1 <= 2) or (2 >= 3) => True
# (1 <= 2) or (2 <= 3) => True
# (1 >= 2) or (2 >= 3) => False

# not	
# Reverses the true-false value of the operand	
# not True => False
# not False => True
# not 1 >= 2 => True
# not 1 <= 2 => False
# not (1 <= 2 and 2 >= 3)  => True
# not 1 <= 2 and 2 >= 3 => False



#_____LOOPS_____# 


# Loops with range:

# If we want to iterate through numbers, we can use Python's for loop and range function. Let's learn how this works by comparing how for loops worked in JavaScript:

# JS: for (var x = 0; x < 10; x += 1){}
# PY: for x in range(0, 10, 1):

# forcopy x in range(0, 10, 1):
for x in range(0, 10):	# increment of +1 is implied
for x in range(10):	# increment of +1 and start at 0 is implied

# Note that if you need to specify an increment other than +1, all three arguments are required.

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Loops through lists.

# If we want to iterate through a list, we could use the range function and send in the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list in order, we can actually loop to get the values of the list directly!

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

# Loops through dictionaries.

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

# That means if we want the values of our dictionary, we might do something like this:

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding:

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc.

# While loops

# While loops are another way of looping while a certain condition is true.

# While:

# Remember this for loop?:
for count in range(0,5):
    print("looping - ", count)

# We can rewrite it as a while loop:

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# The basic syntax for a while loop looks like this:

while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

# Else:

# There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use an else statement with our while loop. Yes, that is right, else in a loop.

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# Note that this ELSE code section is only executed if the WHILE loop runs normally and its conditional is false (whether we never entered the WHILE loop, or we did but eventually the conditional changed from true to false). If instead our WHILE loop is exited prematurely because of a break or return statement, then the else code section will never be executed.

# Loop control 

# We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

# When you want finer control over your loops, use the following statements to do so:

# Break - The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

# The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop. 

# When loops are nested, a break will only exit from the innermost loop.

# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

# Continue - The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

# The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1



#_____FUNCTIONS_____#



# A function is a named block of code that we can execute to perform a specific task. More simply, a function is a list of instructions that we can run at any time and as many times as we would like. If we find something that we seem to be using over and over again, it might be best to have a way to streamline the process. A function:

# has a name
# takes in parameters. (parenthesis required, parameters optional)
# perform a series of instructions
# return something afterwards( will return none if there is no explicit return statement)

# Think of the function as a factory. If we were building a new car we would:

# 1. Specify the features (variables) needed for creating a car.
# 2. Send the specific features (pass arguments) to a car manufacturing plant (invoke function).
# 3. The factory (function) receives the specifications (parameters) and does something with them.
# 4. The factory sends a car (return) back to us, since we sent in the request.

# The factory has all the instructions to build a new car and will perform all the tasks. When you want a new car, all you have to do is call the factory to request a new car.

# The advantages of using functions are:

# Reducing the duplication of code.
# Breaking down complex problems into simpler pieces.
# Improving clarity of code.

# Syntax

# The def keyword signifies the declaration of a function. This indicates that the following code is a function and assigns a name to that function, so we can call it later. Parameters are inputs the function is expecting and appear inside the parenthesis that follow the function name.

# Here's a basic example of a function:

def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# processcopy
    return x	# return value: x

# We have declared a function with the def keyword, named it add, and specified that it takes two inputs (parameters). If this is all we have in our file, nothing would actually appear to happen if we ran it. To actually run the function, we must execute it by invoking or calling it. This is done outside of the function using the function name followed by (). Inside the parenthesis are any values (arguments) the function is expecting as input.

# new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8.

# Once invoked, a function can give us an output. Some functions take an input and some functions don't give us an output. Even if no output is produced, the code inside the function can alter the program - this is called a side effect. Based upon what we learned above, a function that doesn't return anything would produce no output!

# Parameters and Arguments 

# We define the input of functions using parameters. Functions can have as many parameters as we need, including 0. Here we've defined the say_hi function with one parameter called name:

# def say_hi(name):
    print("Hi, " + name)

# Now, we can invoke this function by calling its name and passing in the correct number of arguments:

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. We define parameters. We pass in arguments into functions.

# Return Values

# So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can use later in our program. The following concept is critical in understanding how to use functions correctly in your code:

# It is very important to remember the following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.

# Let's modify our original say_hi function and observe the differences:

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

# Returning a value from a function allows us to store that value in a variable. In this example, we invoked the say_hi function with "Michael" and set it to the greeting variable. When we print greeting we see that it contains the returned value of the say_hi function - "Hi Michael".

# Going back to our add function, recall that it takes two parameters and returns the sum of the parameters.

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2



#______DEFAULT PARAMETERS AND NAMED ARGUMENTS______#



# With the functions we've written so far, we've had to provide the exact number of arguments specified when calling the function. However, if we'd like to allow some of the parameters to be optional to the caller of the function, we can set defaults. Take the following function as an example. The purpose of the function is to take a name and a number and print "good morning {some_name}" to the terminal the given number of times. If no name or number is given, the name is blank and the number is 2, respectively.

def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful()				# output: good morning (repeated on 2 lines)
beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)

#______ROUTING______# #________FLASK_______#

# Routes #

# Routes are an essential part of any web application. A route is much like a variable name we assign to a request. The job of a route is to communicate to the server what kind of information the client needs. This route name is attached to a route on our server that points towards a specific set of instructions. These instructions contain information about how to interpret the data being sent, the operations that need to be completed, and the response that should be sent back. These instructions are the code we'll be creating!

# Every route has two parts:

# 1. HTTP method (GET, POST, PUT, PATCH, DELETE)
# 2. URL

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
# app.run(debug=True) should be the very last statement! 

# Now we have 2 routes--if the client requests localhost:5000/, the hello_world function will run. But if the client requests localhost:5000/success, the success function will run.

# What if we wanted to be able to say "Hello, Michael" or "Hello, Amy" or "Hello, Wes"? We could make three routes, but that feels pretty repetitive. Also, every time we want to include someone else, we would need to create a new route. This is a great opportunity to add variable rules to our routes. For the example above, we could make the name a variable, like so:

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

# We can add as many of these as we need, giving each variable a different name:

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# The localhost:5000 part of the route determines which server to call upon. The rest of the route, including the "/", tells the server which function should be invoked.

# Although the code we show above is brief, we're bringing together a lot of concepts you've never seen before. Test out all the code snippets we've given you to this point to make sure you understand how everything's working. While it doesn't do much, you've created your first web application!



