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
# courses = ['History', 'Math', 'Physics', 'CompSci']
# nums = [9, 7, 4, 5, 8, 1]

# # convert nums into list of strings
# num_strs = [str(num) for num in nums]
# print("Step 1:", num_strs)

# # join list of strings into a single string separated by ' - '
# num_str = ' - '.join(num_strs)
# print("Step 2:", num_str)

# # split string back into a list of strings
# lis = num_str.split(' - ')
# print("Step 3:", (lis))

# # convert list of strings back into list of integers
# lis = [int(num) for num in lis]

# print("Step 3:", lis)
# -------------------------------------------------
# Write a function that receives a tuple as input. The tuple might include duplicates. 
# Convert the tuple to a set which will remove duplicates automatically. 
# Then convert the set to a list. Then sort the list. 
# Then create a new list that includes the items in the previous list, each one duplicated as many times as its index. 
# For instance, the first item in the list would appear only once in the new list, 
   # the second item in the list would appear two times in the list, etc. 
# Then it prints the new list and returns the new list. For instance, if the input is ('b', 'a', 'c', 'a', 'c'), 
# the output should be ['a', 'b', 'b', 'c', 'c', 'c']. If the input is (8, 5, 6, 6), the output should be [5, 6, 6, 8, 8, 8].

# tup = ("a", "a", "a", "b", "c", "d", "e", "f", "g")

# def Geometric(tup):
#     tup_to_set = set(tup)
#     set_to_lis = list(tup_to_set)
#     set_to_lis.sort()

#     new_list = []
#     dup = 0
#     for letter in set_to_lis:
#         dup = dup + 1
#         new_list.append(letter * dup)
#     return new_list

# print(Geometric(tup))
#-----------------------------------------------------
