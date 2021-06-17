

# Book Index
# Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges.

# Given [1, 3, 4, 5, 7, 8, 10],
# return the string "1, 3-5, 7-8, 10".
# """
# def book_index(arr):
#     pass

# print(book_index([1, 3, 4, 5, 7, 8, 10]))
# # "1, 3-5, 7-8, 10"

def book_index(arr):
    result = str(arr[0])
    is_range = False
    if arr[0] == arr[1] - 1:
        is_range = True
        result += '-'
    else:
        result += ', '

    for x in range(1, len(arr)-1):
        # print('in loop')
        if is_range == False:
            result += str(arr[x])
        if arr[x] + 1 != arr[x + 1]:
            print('in if')
            is_range = False
            result += f"{arr[x]}, "
        elif arr[x] == arr[x + 1] - 1:
            print('in elif')
            if is_range != True:
                result += '-'
            is_range = True
        else:
            print('in else')

    result += str(arr[len(arr)-1])
    return result

print(book_index([1, 3, 4, 5, 7, 8, 10, 11]))