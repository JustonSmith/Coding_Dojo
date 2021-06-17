def r_fibonacci(num):
    if num <=1:
        return num
    # print(num)
    return r_fibonacci(num-2) + r_fibonacci(num-1)

# Recursive Fibonacci

# Write rFib(num). Recursively compute and return the numth Fibonacci value. As earlier, treat the first two (num = 0, num = 1) Fibonacci values as 0 and 1.
# rFib(2)
# 1 (0+1)
# rFib(3)
# 2 (1+1)
# rFib(4)
# 3 (1+2)
# rFib(5)
# 5(2+3)