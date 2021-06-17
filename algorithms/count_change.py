c=int(input('Please enter an amount between 0-99:'))
print(c//25, "quarters")
c = c%25
print(c//10, "dimes")
c = c%10
print(c//5, "nickles")
c = c%5
print(c//1, "pennies")