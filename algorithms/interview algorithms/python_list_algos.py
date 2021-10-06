#
#
#
#
#
### LIST ALGOS ###
#
#
#
# 
# 
# # SWAP FIRST AND LAST POSITION #

# Given a list, write a python progran to swap the first and last element of that list.

# Input = [12, 35, 9, 56, 24]
# Output = [24, 35, 9, 56, 12]

# Input = [1, 2, 3]
# Output = [3, 2, 1]

# Approach 1: Find the length of the list and simply SWAP the first element with (n-1)th element.


from typing import List


def swap_list(new_list):
    size = len(new_list)

    # swapping
    temp = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1] = temp

    return new_list

# Driver code
new_list = [12, 35, 9, 56, 24]

print(swap_list(new_list))


# Approach 2: The last element of the list can be referred to as list[-1]. Therefore we can simply swap list[0] for list[-1].

def swap_list_2(new_list_2):
    new_list_2[0], new_list_2[-1] = new_list_2[-1], new_list_2[0]

    return new_list_2

# Driver code
new_list_2 = [12, 35, 9, 56, 24]
print (swap_list_2(new_list_2))


# Approach 3: Swap the first and last element using a tuple variable. Store the first and last element as a pair in a tuple variable, say get, and unpack those elements with the first and last element in that list. Now, the first and last values in that list are swapped.

def swap_list_3(list) :
    
    # storing the first and last element as a pair in a tuple variable get.
    get = list[-1], list[0]

    #unpacking those elements
    list[0], list[-1] = get

    return list


# Approach 4: Using * opperand. This opperand proposes a change to iterable unpacking syntax, allowing to specify a "catch-all" name which will be assigned a list of all items assigned to a "regular" name.

list_4 = [1, 2, 3, 4]

a, *b, c = list_4

print(a)
print(b)
print(c)

# Implementation of approach 4.

def swap_list_4(list_4):
    start, *middle, end = list_4
    list_4 = [end, *middle, start]

    return list_4

# Driver code
new_list_4 = [12, 35, 9, 56, 24]

print(swap_list_4(new_list_4))


# Approach 5: Swap the first and last elements using built-in function list.pop(). Pop the first element and store it in a variable. Similarly, pop the last element and store it in another variable. Now insert the two popped element at each others original position.

def swap_list_5(list_5):

    first = list_5.pop(0)
    last = list_5.pop(-1)

    list_5.insert(0, last)
    list_5.append(first)

    return list_5

new_list_5 = [12, 35, 9, 56, 24]
#
# 
# 
# 
# 
# # SWAP TWO POSITIONS #
#
#
#
#
#
# given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]


# Approach 1: Simple swap using comma assignment. Since t

def swap_positions(list_1, pos1, pos2):

    list_1[pos1], list_1[pos2], list_1[pos1]

    return list_1

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swap_positions(List, pos1-1, pos2-1))


# Approach 2: Using built in list.pop() function

# Pop the elemenet at pos1 and store it in a variable. Similarly, pop the element at pos2 and store it in another variable. Now insert the two popped elements at each other's original position.

def swap_positions_2(list_2, pos1_2, pos2_2):

    # popping both elements from the list

    first_element = list_2.pop(pos1_2)
    second_element = list_2.pop(pos2_2-1)

    # inserting in each other's positions

    list_2.insert(pos1_2, second_element)
    list_2.insert(pos2_2, first_element)

    return list_2

# Driver function
List = [23,65,19,90]
pos1_2, pos2_2 = 1, 3

print(swap_positions_2(List, pos1_2-1, pos2_2-1))


# Approach 3: Store the element at pos1 and pos2 as a pair in a tuple variable, say GET. Unpack those elements with pos2 and pos1 positions in that list. Now, both the positions in that list are swapped. 


def swap_positions_3(list_3, pos1_3, pos2_3) :

    # Storing the two elements as a pair in a tuple variable "get".
    get = list_3[pos1_3], list_3[pos2_3]

    #unpacking those elements
    list_3 = [pos2_3], list_3[pos1_3]

    return list_3

# Driver code

List = [23, 65, 19, 90]

pos1_3, pos2_3 = 1, 3

print(swap_positions_3(List, pos1_3-1, pos2_3-1))
#
#
#
#
#
# ### FIND THE LENGTH OF A LIST ###
#
#
#
#
#
# List being an integral part of Python day-to-day programming has to be learned by all python users and have a knowledge of its utility and operations is essential and always a plus. 

# APPROACH 1: Naive method.

# In this method a loop is run and the counter increases until the last element of the list is counted. This is the most basic strategy that can possibly be employed in the absence of other preset techniques.

# Initializing list
test_list = [1, 4, 5, 7, 8]

#printing test list
print ("The list is : " + str(test_list))

#Finding length using loop and counter.
#Initializing counter

counter = 0
for i in test_list :
    counter = counter + 1

print ("Length of list using naive method os : " + str(counter))


# Approach 2: using len().


#The len() method offers the most used and easiest way to find the length of any list. This is the most conventional technique adopted by programmers.


a = []
a.append("Hello")
a.append("Nerds.")
a.append("Make")
a.append("my")
a.append("day.")

print("The length of the list is : ", len(a))

n = len([10, 20, 30])
print("The length of the list is : ", n)
# 
# 
# 
# 
# 
# ### Maximum of two numbers ###
#
#
#
#
#
# Given two numbers, write a program to find the maximum of these two numbers.

# Approach 1:

def maximum_1(a, b) :

    if a >= b:
        return a
    else:
        return b

# Driver code
a = 2
b = 4
print(maximum_1(a, b))


# Approach 2: Using the max() function.
# This function is used to find the maximum of the valuse passed through its arguments.

a = 2
b = 4

maximum_2 = max(a, b)
print(maximum_2)

# Approach 3: Using Ternary Operator.
# This operator is also known as a conditional expression. These are operators that evaluate something based on a condition being true or false. It simply allows testing in a single line.

# Driver code
a = 2
b = 4

# Use of ternary operator
print(a if a >= b else b)
# 
# 
# 
# 
# 
# ### MINIMUM OF TWO NUMBERS ###
# 
# 
# 
# 
# 
# Given two numbers, write a program to find the minimum of these two numbers.


# Approach 1: This is the naive approach where we will compare numbers using if-else.

def minimum_1(a,b) :
    if a <= b :
        return a
    else :
        return b

# Driver code
a = 2
b = 4

print(minimum_1(a, b))


# Approach 2: Using the min() function.

a = 2
b = 4

minimum_2 = min(a, b)
print(minimum_2)





