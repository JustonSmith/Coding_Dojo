#
# For loop basics II #

# 1. Biggie Size: Given a list, write a function that changes all positive numbers in the list to "big". 
# Ex: biggie_size([-1, 3, 5, -5]) = [-1, "big", "big", -5]

def biggie_size():
    big_list = []
    for size in range(0, len(big_list)):
        if size > 0:
        return "big"

print biggie_size([-1, 3, 5, -5])

# 2. Count Positives:  
# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives():
    positive_list = []
    positive_count = 0
    for positive_number in range(0, len(positive_list)):
        if positive_number >= 0
        positive_count += 1
    
    len(positive_list - 1) = positive_count
    return positive_count

print count_positives(positive_count)

# 3. Sum Total:
# Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(l):
    sum = 0
    for val in l:
        total = total + val
    return total

my_list = [1, 2, 3, 4]
print sum_total(my_list)

# 4. Average:
# Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(num):
    sum_num = 0
    for total in num:
        sum_num = sum_num + total
    avg = sum_num / len(num)

print(average([1, 2, 3, 4]))

# 5. Length:
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0


def length(idx):
    count = 0
    for i in range(len(idx))
    count += 1
    return count

idx = [1, 2, 3, 4]
print(length(idx))

# 6. Minimum: 
# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(list):
    current_min = list[0]
    for num in list:
        if num < current_min:
        current_min = num
    return current_min

print minimum([1,2,3,-1])

# 7. Maximum: 
# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(list):
    current_max = list[0]
    for num in list:
        if num > current_max:
        current_max = num
    return current_max

print maximum([1,2,3,-1])

# 8. Ultimate Analysis:
# Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False.

# 9. 
def reverse_string(str):
    reversed = ""
    for i in range(len(str)-1, -1, -1):
        reversed += str[i]
    return reversed

print(reverse_string('Welcome to Python!'))

for i in range(len(list)):








