
# Problem 1: Return true of one of them is 10, or the sum of a + b is 10
def ifTen(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False

a = 6
b = 7
#print(ifTen(a, b))

# Problem 2: Given integers a and b, return True if either one is 6. Or if their sum or difference is 6.
# The difference is always 6. 7 - 1 = 6 and 1 - 7 = 6
def Difference6(a, b):
    if a == 6 or b == 6:
        return True
    elif a + b == 6:
        return True
    elif a - b == 6:
        return True
    elif b - a == -6:
        return True
    else:
        return False

# print(Difference6(a, b))

# Problem 3: Given a non-empty string and an int n, return a new string where the
# character at index n has been removed.

str = "Adrian"

n = 4

def RemoveNIndex(str, n):
    new_str = ''
    for index, value in enumerate(str):
        if n == index:
            continue
        new_str = new_str + value
    return new_str
 
#print(RemoveNIndex(str, n))

# Problem 4: Given a list of ints, return True if the list contains a 2 next to a 2 somewhere

nums = [1, 2, 2, 3, 4, 5, 6]

# def ConsTwo(nums):
#     cons = 0
#     for num in nums:
#         if num == 2:
#             cons = cons + 1
#         else:
#             cons = 0
#         if cons == 2:
#             return True
#     return False

# or 

def has_two_adjacent(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1] == 2:
            return True
    return False


#print(has_two_adjacent(nums))


# Problem 5: Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences

def AppearAtEnd(str1, str2):
    LowerStr1 = str1.lower()
    LowerStr2 = str2.lower()
    if LowerStr1.endswith(LowerStr2) or LowerStr2.endswith(LowerStr1):
        return True
    else:
        return False

#print(AppearAtEnd(str1="Hello", str2="lx"))

# Problem 6: Flatten a list, write a function that takes a list and flattens it into a one-dimensional list.

lis = [[1, 2], [3, 4], [5, 6]]

def Flatten(lis):
    new_list = []
    for sublist in lis:
        for element in sublist:
            new_list.append(element)
    return new_list

# print(Flatten(lis))

# Problem 7: Two strings are anagrams if you can make one from the other by rearranging the letters.
# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and false otherwise.
# For example, the call is_anagram("typhoon", "apython") should return True, while ("Alice, Bob") should return false.
# (I added extra capitalzation step)

str1 = "Adrian"
str2 = "ADRIAN"

def is_anagram(str1, str2):
    sort_str1 = sorted(str1.lower())
    sort_str2 = sorted(str2.lower())
    if sort_str1 == sort_str2:
        return True
    return False

#print(is_anagram(str1, str2))

# Problem 8: Return True if the given string contains an appearance of "xyz" where the "xyz"
# is not direclty proceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


def PeriodInXYZ(string):
    for i in range(len(string) - 2):
        if string[i] == "x" and string[i - 1] != ".":
                if string[i + 1] == "y":
                    if string[i + 2] == "z":
                        return True
    return False
                    
# print(PeriodInXYZ(string))


# # Problem 9: Write a function named format_number that takes a non-negative number as its only parameter.
# # Your function should convert the number to a string and add commas as a thousands operator.
# # For example, calling format_number(1000000) should return "1,000,000".

num = 1009

def format_number(num):
    if num < 0:
        return "Use a positive number."
    
    num_str = str(num)
    new_num = ''
    reverse_string = num_str[::-1]

    for i in range(len(reverse_string)):
        if i % 3 == 0 and i != 0:
            new_num = reverse_string[i] + "," + new_num
            continue

        new_num = reverse_string[i] + new_num
    return new_num

print(format_number(num))


# Problem 10: Make a tic tac toe game that plays with the user.

lis = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(lis[1][2])
