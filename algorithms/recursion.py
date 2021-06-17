"There are three requirements for effective recursion, as follows:"

a) "Base cases:"
"When a function can determine (and return) an answer immediately, this is a ‘base case’. If you successfully guessed my number, we know right away the game is over. Conversely, if you look for ‘spizzwink’ in a dictionary and find no word between ‘spitz’ and ‘splash’, you know ‘spizzwink’ is not in that dictionary. There are positive base cases and negative base cases."

b) "Forward progress:
"If a function cannot solve a problem but can narrow the range of possibilities, this is ‘forward progress’. Learning that guess ‘60’ is too high, you have made forward progress because you now know the solution is not in the ‘60-120’ range. Generally, for recursion to be effective, you must make at least a little forward progress in all cases. If there is a case in which you can neither solve the problem nor break it down further, you cannot solve the problem in all cases."

c) "Calling back into itself as if it were the original problem:"
"What if earlier my initial challenge had been “I’m thinking of an integer between 1 and 59 -- guess it!” You would have proceeded exactly as you did in the original ‘1-120’ problem, after learning that ‘60’ was too high. If each guess were a function call, then after learning that ‘1-120’ could be limited to ‘1-59’, you could call the function again with ‘1-59’ as if it were the original 126 challenge. Furthermore, this function wouldn’t know whether this request was the initial challenge, or a subsequent call to itself after narrowing things down! A recursive function behaves correctly either way, so it doesn’t know or care about this distinction.
[9:30 AM]"
# Recursion

# 1.) Recursive call (function that calls itself)

def my_func():
    my_func()

# 2.) Forward progress

# 3.) Break case (condition)
    # return



def print_num():
    for x in range(1, 5, 1):
        print('x is:', x)


# print_num()

def r_print_num(x=1):
    if x == 5:
        # break case
        return

    x += 1
    r_print_num(x)
    print('x is:', x)

r_print_num()








def r_sigma(num):
    if num <= 1:
        return num + r_sigma(num - 1)
    # Write a recursive function that, given a number, returns the sum of integers from one up to that number. For example, rSigma(5) = 1+2+3+4+5 = 15; rSigma(2.5) = 1+2 = 3; rSigma(-1) = 0


print(r_sigma(8))
# 36




def r_factorial(num):
    if num <=1:
        return num
    return num * r_factorial(num - 1)
    # Given a number, return the product of integers from 1 upward to that number. If less than zero, treat as zero. If not an integer, treat as an integer. Mathematicians tell us that 0! is equal to 1, so make
    pass

print(r_factorial(4))
# 24