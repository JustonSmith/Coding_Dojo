#
# 
#

# def getDigits(str):
#     newStr = []
#     for i in range(0, len(str)):
#         if type(str[i]) == int:
#             if str[i] % 2 == 0 or str[i] % 2 == 1:
#                 newStr.append(str[i])
#     return newStr

# print(getDigits("[z4d2g5s2]))

# def gotDigits(str):
#     newStr = ""
#     for i in range(len(str)):
#         if str[i] >= "0" and str[i] <= "9":
#                 newStr += str[i]
#     return newStr

# print(gotDigits("z4d2g5s2"))

def isPalindrome(str):
    isPal = True
    for i in range(len(str)):
        if str[i] == str[len(str) - 1 - i]:
            isPal = True
        else: 
            isPal = False
    return isPal

print(isPalindrome('tuesday'))
print(isPalindrome('tacocat'))

