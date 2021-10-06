# 
# 
# 
# 
# 
# ### STRING ALGOS ###
#
#
#
#
#
# Check whether string is symmetrical or a palindrome.
# A string is said to be symmetrical is both the halves of the string are the same, and a string is said to be a palindrome if one half of the string is the reverse of the other half. The same forwards as backwards.

# Approach 1: Naive. A loop is run to the mid of the string and the first and last characters are matched. If the characters are not similar then the loop breaks and the string is not a palindrome. Otherwise the string IS a palindrome. 

# In the case of symmetry, if the string length is even then the string is broken into two halves and the loop is run, checking the characters of the strings of both the half. If the characters are not similar then the loops break and the string is not symmetrical otherwaise the string IS symmetrical. If the string length is odd then the string is broken into two halves in such a way that the middle element is left unchecked, and the above step is repeated.


# Implementation :

# Function to check whether string is a palindrome

def palindrome(a) :

    #finding the mid, start and last index
    mid = (len(a)-1)//2 
    start = 0
    last = len(a)-1
    flag = 0

    # loop till the mid of string
    while(start <= mid) :

        # comparing letters from right to letters from left
        if a[start] == a[last] :

            start += 1
            last += 1

        else: 
            flag = 1
            break;

    # checking the flag variable to see if string is a palindrome or not
    if flag == 0 :
        print("The entered string is a palindrome")
    else :
        print("The entered string is not a palindrome")

# Function to check whether the string is symmetrical or not
def symmetry(a) :

    n = len(a)
    flag = 0

    # Check if string length is odd or even
    if n%2 :
        mid = n//2 + 1
    else :
        mid = n//2

    start1 = 0
    start2 = mid

    while(start1 < mid and start2 < n) :

        if (a[start1] == a[start2]) :
            start1 = start1 + 1
            start2 = start2 + 1
        else :
            flag = 1
            break;

    # Check the flag variable to see if string is symmetrical or not

    if flag == 0 :
        print ("The entered string is symmetrical")
    else :
        print ("The entered string is not symmetrical")

# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)


# Approach 2: Slicing method.


string = 'amaama'
half = int(len(string) / 2)

if len(string) % 2 == 0 : # even
    first_str = string[:half]
    second_str = string[half:]
else : # odd
    first_str = string[:half]
    second_str = string[half-1:]

# symmetric

if first_str == second_str :
    print(string, 'string is symmetrical')
else :
    print(string, 'string is not symmetrical')

# palindrome

if first_str == second_str[::-1] :
    print(string, 'string is a palindrome')
else :
    print(string, 'string is not a palindrome')
# 
# 
# 
# 
# 
# ### REVERSE WORDS IN A STRING ###
# 
# 
# 
# 
# 
# Given a string, reverse the worse in said string.

# separate each word in given string using split() method of string data type in python.
# reverse the word separated list.
#print words of list, in string form after joining each word with a space using "".join() method in python.

def rev_sentence(sentence) :

    # first split the string into words
    words = sentence.split('')

    # then reverse the split string list and join using space
    reverse_sentence = ''.join(reversed(words))

    # finally return the jpined string
    return reverse_sentence

if __name__ == "__main__" :
    input = 'geeks quiz practice code'
    print (rev_sentence(input))


