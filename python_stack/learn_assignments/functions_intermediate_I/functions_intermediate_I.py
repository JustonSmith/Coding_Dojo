#
#

#With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.


import random

def rand_int(min= 0 , max= 100):
    if min > max:
        print("Please choose a min that is less than max.")
    elif max < 0:
        print("Please choose a positive number for max")
    num = randon.random() * (max - min) + min
    return round(num)

print(rand_int(min = 500, max = 50))