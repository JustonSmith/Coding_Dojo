# 
# 

# Functions Basic II:

# 1. Countdown - Create a function that accepts a number as an imput. Return a new list that counts down by one, from the number (as the 0th element) down to 0(as the last element).

import time

def countDown(num):
    for i in range(num, 0, - 1):
        print(i)
        time.sleep(1)
countDown(10)
print("Blastoff!")

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second. ex: print_and_return([1,2]) should print 1 and return 2.

def printAndReturn(num1, num2):
    print(num1)
    return(num2)

printAndReturn(5, 10)

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length. Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def firstPlusLength(list):
    a = list[0]
    b = len(list)
    return a+b

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.

def values_greater_than_second(list):
    newList = []
    greater = 0
    for x in range(len(list)):
        if list[x] > list[1]:
            newList.append(list[x])
            greater += 1
        if len(list) <= 2:
            return False
    print(greater)
    return newList
print(values_greater_than_second([1, 2, 3, 4, 5, 6]))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value. Example: length_and_value(4,7) should return [7,7,7,7] Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    newArr = []
    for value in range(size):
        newArr.append(value)
        return newArr
print(length_and_value(4, 7))
