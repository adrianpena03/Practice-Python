# 1 - Given a list of ints, return true if 6 appears as either the first or last element in the list
lis = [2, 3, 4]

# def SixFirstOrLast(lis):
#     if (lis[0] == 6) or (lis[-1] == 6):
#         return True

# result = SixFirstOrLast(lis)
# print(result)

# 2 - Given a list of ints, return the number of 9's in the list
# def ReturnNine(lis):
#     nines = 0
#     for num in lis:
#         if num == 9:
#             nines = nines + 1
#     return nines

# r = ReturnNine(lis)
# print(r)

# 3 - Return the number of even ints in the given list
# def ReturnEven(lis):
#     evens = 0
#     for num in lis:
#         if num % 2 == 0:
#             evens = evens + 1
#     return evens

# print(ReturnEven(lis))

# 4 - Given a sring, return a new string made of every other character starting w the first

word = "Hello"

def EveryOtherChar(word):
    return word[::2]

# print(EveryOtherChar(word))

# 5  - Given a list of ints, return True if one of the first 4 elements in the list is 9. List may be less than 4
ints = [1, 3, 8, 11, 9]
def FirstFourIsNine(ints):
    for num in ints:
        if num < 4:
            if 9 in ints:
                return True
        else:
            if 9 in ints[0:5]:
                return True
        
print(FirstFourIsNine(ints))

# 6 - Given a list of ints, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere

# Given a string of Lowercase alphabetical characters, return a new string with the characters 