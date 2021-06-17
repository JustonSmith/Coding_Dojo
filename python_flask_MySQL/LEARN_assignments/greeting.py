# #
# # 
# # Greetings:

# # Part 1: Write a program that asks for a users name, and greets them with their name.

# greeting = input('What is your name?')
# print(f'my name is: {greeting}')

# # Part 2: If the name given is the same as your name, say "Hey thats my name!"

# Greeting = input('What is your name?')
# print(f'my name is: {greeting}')
# if greeting == 'Juston':
#     print('Hey thats my name too')

# #Part 3: Ask for 10 names and keep a record of them.  After 10 names are given, say 'It was nice to meet all of you'.

# personal_names = []
# for names in range(10):
#     greeting = input('what is your name?')
#     personal_names.append(greeting)
# print('It was nice to meet all of you')

# # Part 4 - NINJA Level:
# # Ask for 10 names again.  This time check to see if the name was already given.  If it hasn't greet them other wise ask for a new name.  At the end of the program, you should have greeted 10 unique names.
personal_names = []
for names in range(10):
    greeting = input('what is your name?')
    if greeting == personal_names + [names]:
        print('Your name has already been given')
    else: personal_names.append(greeting)
    print('It was nice to meet all of you') 
