
# Acronym Algo

# Given a string of words, return an acronym of the words in the original string.
# Input => "Thank goodness it's Friday"
# Output => "TGIF"

class Solution:
    def solve(self, s):
        tokens = s.split()
        string = ""
        for word in tokens:
            if word != "and":
                string += str(word[0])
        return string.upper()
ob = Solution()
print(ob.solve("Live from New York, it's Saturday Night!"))