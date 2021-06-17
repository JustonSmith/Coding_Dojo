

init_strlist = ["ovation", "notation", "action"]
def common_suffix(arr):
    newString = ""
    current_character = ""
    is_match = True
    x = 1
    while is_match = True
        for word in arr:
            if current_character == "":
                word[len(word - 1)]
                elif word[len(word) - 1] != current_character:
                    # false
        
                str = str [len(arr) - 1]
        newString = current_character + newString
        current_character = ""

print(common_suffix("ovation", "notation", "action"))


# Braces

def braces_valid(string):
    count = 0 
    track ""
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "{" or string[i] == "[":
            count += 1
            track += string[i]
        elif string[i] == ")" or string[i] == "{" or string[i] == "]":
            