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
word = "Hello World"

print(word[-1:-5:-1])