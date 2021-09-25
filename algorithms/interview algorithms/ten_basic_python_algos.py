



### TEN BASIC INTERVIEW ALGORITHMS ###

# 1. REVERSE INTEGER

# Given an integer, return the integer with reversed digits.
# NOTE: The iteger could be either positive or negative.

def solution(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string [:0:-1])
    else:
        return int(string[::-1])

print(solution(-231))
print(solution(345))


# 2. AVERAGE WORDS LENGTH


# For a given sentence, return the average word length.
# NOTE: Remember to remove the punctuation first.

sentence1 = "Hi all, my name is Tom. I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution(sentence):
    for p in "!?'.;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

print(solution(sentence1))
print(solution(sentence2))


# 3. ADD STRINGS

# Given two non-negative integers num1 and num2 represented as a string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# NOTE:

# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero.

num1 = '364'
num2 = '1836'

# Approach 1:

def solution(num1, num2):
    eval(num1) + eval(num2)

print(solution(num1, num2))

# Approach 2:
# Given a string of length one, the ord() function returns an integer representing the unicode point of the character.
# When the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.

def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1/10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)
print(solution(num1, num2))


# 4. FIRST UNIQUE CHARACTER

# Given a string, find the first unique character in it and return its index.
# IF it doesnt exist, return -1. # Note: all the input strings are already lowercase.


# Approach 1:

def solution(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] += 1
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i

        return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

print('###')

#Approach 2:

import collections

def solutions(s):
    # build hash map : character and how often it appears
    count = collections.Counter(s) # <--- gives back a dictionary with words occurance count
                                        # Counter({'l': 1, 'e': 3, 't':1, 'c':1, 'o':1, 'd': 1})

# Find the index
    for idx, ch in ennumerate(s):
        if count[ch] == 1:
            return idx

    return -1

print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))


# 5. VALID PALINDROME

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The srting will only contain lowercase characters a-zpygame.examples.mask.main()

s = 'radkar'
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True

    return s == s[::-1]

solution(s)


# 6. MONOTONIC ARRAY

# Given an array of integers, determine whether the array is monotonic or not.

A = [6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7]

def solution(nums):
    return  (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            (all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))))

print(solution(A))
print(solution(B))
print(solution(C))


# 7. MOVE ZEROES

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.

array1 = [0,1,1,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def solution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

solution(array1)
solution(array2)


# 8. FILL THE BLANKS

# Given an array containing None values fille in the None values with most recent non None value in the array. 
array1 = [1, None, 2, 3, None, None, None, 5]

def solution(array):
    valid = 0
    res = []
    for i in nums:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
        return res

solution(array1)


# 9. MATCHED AND MISMATCHED WORDS

# Given two sentences, return an array that has the words appear in one sentence and not the other and an array with the words in common.

sentenceA = 'We are really pleased to meet you in our city.'
sentenceB = 'The city was hit by a heavy storm.'

def solution(sentenceA, sentenceB):
    set1 = set(sentenceA.split())
    set2 = set(sentenceB.split())

    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

print(solution(sentenceA, sentenceB))


# 10. PRIME NUMBERS ARRAY

# Given k numbers which are less than n, return the set of prime numbers among them.
# NOTE: The task is to write a program to print all Prime numbers in an interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than on and itself. 

n = 35
def solution(n):
    prime_nums = []
    for num in range(n):
        if num > 1: # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0: # if the modulous == 0 it means that the number can be divided by the number preceeding it. 
                    break
            else: 
                prime_nums.append(num)
    return prime_nums
solution(n)