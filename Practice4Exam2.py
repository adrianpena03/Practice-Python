# Given a string, return a string where for every character in the original, 
# there are two characters. 
# Closer to difficulty of problem in exam

# def DoubleLetter(word):
#     New_String = ""
#     for i in range (len(word)):
#         index = word[i]
#         New_String = New_String + index * 2
#     return New_String

# result = DoubleLetter("Adrian")

# ----------------------------------------------------

# Write a function called Eight_count(bin) that receives a string consisting of
# only eights and nines as arguments and returns the biggest number of 
# consecutive eights in the string

# bin = "998889"

# def Eight_Count(bin):
#     count = 0
#     biggest = 0
#     for i in bin:
#         if i == "8":
#             count += 1
#         else:
#             if count >= biggest:
#                 biggest = count
#             count = 0
#         if count >= biggest:
#             biggest = count
#     return biggest            

# result = Eight_Count(bin)
# print(result)

# def eight_count(bin):
#      cons = 0
#      biggest = 0
#      for eights in bin:
#           if eights == "8":
#                cons = cons + 1
#           else:
#                if cons >= biggest:
#                     biggest = cons
#                     cons = 0
#           if cons >= biggest:
#                biggest = cons
#      return biggest

# result = eight_count(bin)
# print(result)

#------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [9, 7, 4, 5, 8, 1]

# convert nums into list of strings
num_strs = [str(num) for num in nums]
print("Step 1:", num_strs)

# join list of strings into a single string separated by ' - '
num_str = ' - '.join(num_strs)
print("Step 2:", num_str)

# split string back into a list of strings
lis = num_str.split(' - ')
print("Step 3:", (lis))

# convert list of strings back into list of integers
lis = [int(num) for num in lis]

print("Step 3:", lis)
# -------------------------------------------------
#Write a function that takes two lists of integers as input 
# and returns a new list containing the elements that appear in 
# both lists, in the order they appear in the first list.

# For example, if the first list is [1, 2, 3, 4, 5] and the 
# second list is [3, 6, 2, 8, 7], the output list should be 
# [2, 3], because those are the elements that appear in both lists, 
# in the order they appear in the first list.

# Your function should take two arguments, which are the input 
# lists, and return a single value, which is the output list.
# If an element appears more than once in the first list, it should 
# only appear once in the output list.

nums_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
nums_2 = [1, 3, 4, 7, 4, 3, 8, 9, 10, 3]

def OnlyEven(nums):
    similar = []
    # for loop that iterates through num_1
        # for loop that iterates through num_2
            # if number in num_1 == num_2
                # append number from num_1 to similar list
            # else
                # continue
    # return similar list