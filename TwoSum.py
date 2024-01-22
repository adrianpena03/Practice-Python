# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# target = 10

# def twoSum(target, num):
#     for i in num:
#         for j in num:
#             if i + j == target:
#                 return num[i], num[j]
#             return "Not Found"

# print(twoSum(target, num))


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 10, 15, 20]

def Consecutive(nums):
    cons = 0
    biggest = 0
    

print(Consecutive(nums))

# iterate through
# check if next number is + 1 
# if next number is + 1 from the previous, cons = cons + 1
# if next number is the same as the previous, continue
# if next number is not + 1, then check if biggest > cons, if it is, then do nothing, else, biggest = cons, cons = 0
# contine to iterate through list