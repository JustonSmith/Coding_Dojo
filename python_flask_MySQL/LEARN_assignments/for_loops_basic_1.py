# 
# 
# For Loops Basic 1:
# 
# 

# 1. Basic: Print all integers from 0 to 150.

for nums in range(151):
    print(nums)

# 2. Multiples of 5: Print all the multiples of 5 from 5 to 1,000.

for nums in range(1001):
    if nums % 5 == 0:
        print(nums)

# 3. Counting, the Dojo Way: Print integers 1 to 100. If divisible by 5 print "Coding"

for nums in range(101):
    if nums % 10 == 0:
        print("Coding Dojo")
        continue
    elif nums % 5 == 0:
        print("Coding")

# 4. Whoa, That Sucker is Huge: Add odd integers from 0 to 500,000, and print the final sum.

maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for nums in range(1, maximum+1):
    if(nums % 2 != 0):
        print("{0}".format(nums))
        Oddtotal = Oddtotal + nums

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(nums, Oddtotal))

# 5. Countdown by fours: Print positive numbers starting at 2018, counting down by fours.

countdown = 2018
while countdown > 0:
    print('countdown = ', countdown)
    countdown = countdown - 1

# 6. Flexible Counter: Set three variables, lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines).

lowNum = 2
highNum = 9
mult = 3

for nums in range(lowNum, highNum):
    if nums % mult == 0:
        print(nums)