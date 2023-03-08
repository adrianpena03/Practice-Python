# Me-21 = "Hi" - Not allowed bc dash
# 2Em = 'Hi' - Not allowed bc starts w number
# variables can only contain letters, numbers, and underscores

# message = 'John\'s Book'
# message = 'John\s Book'
# message = "John\'s Book"
# print(message)
# escape character python, counts as 1

# message = "John\\\s Book"
# message = "John\\\\s Book"
# print(message)
#
# message = "Hello World"
# print('len(message): ', len(message))
#
# print('message[0]', message[0]) # indexing uses brackets
#
# #print(message[len(message)]) # - QUESTION ON EXAM
#
# print('message[len(message)-1: ', message[len(message)-1])
#
# print("Message Last Letter: ", message[1:6:7])
# print('message[:5]: ', message[:5])
#
# print('message[0:0]: ', message[1:6:2]) # 2 means take 2 steps
#
# print('message[0:0]: ', message[2::-1])
# print('message[0:0]: ', message[::-1])

# message = "Hello World"
# print(message.count('hello')) # Will not get error, will be 0 if doesn't exist
# print(message.count("Hello")) # Prints 1
# print(message.find("Hello")) # Prints 0 bc of index


# Given a string name, e.g. 'Bob', return a greeting of the form 'Hello Bob!'.

# def Greeting(name):
#     return "Hello " + name + "!"
#
# # P2: Given a string and a non-negative int n, return a larger string that is n # copies of the original string
#
# def Larger(string, n):
#         return string * n
#
#
# # Given a string and a non-negative int n, we'll say that the front of the string is the first 3 characters
# # or whatever is there if the string is less tha length 3. Return the n copies of the front.
#
# def func3(word, n):
#     front = " "
#     if len(word) < 3:
#         front = word
#     else:
#         front = word[0:3]
#     return front * n
#
# # Given a string, return a string where for every character in the original, there are two characters. Closer to difficulty of problem in exam
# def DoubleLetter(str):
#     new_string = " "
#     for i in str:
#         new_string += i*2
#     return new_string
#
# # OR
#
# def Double_Char(str):
#     return " ".join([c * 2 for c in str])

# Write a function called Eight_count(bin) that receives a string consisting of only eights and nines as arguments
# and returns the biggest number of consecutive eights in the string

#courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses)
# #print (courses[4]) # error
# courses [0] = 100
# print(courses) # Gets rid of history element
# courses.insert(2, 'Chemistry')
#
# courses_2 = ['Art', 'Chemistry']
# courses.insert(2, courses_2)
# #courses.extend(courses_2) # Adds individual elements to first list
# #courses.append(courses_2) # Adds whole set of elements to first list (brackets included, same with insert)
# print(courses[2][0])
#
# output = courses.remove('Math')
# print(output) # PRINTS NOTHING
#
# # But if you put
# print(courses) # Math is gone
#
#
#
# output = courses.pop(1) # returns value that was removed from list
# print(courses)
#
# output = courses.pop() # removes last element of the list
#
# print(courses.reverse()) # This by itself prints nothing
# print(courses) # prints the reverse bc course.reverse is an in place function

#courses.sort(reverse = True) # sorts then reverses

#print(sorted(courses)) # returns the sorted list, but doesn't change the course itself

#print(max(courses)) # Return Max Letter in alphebetical order
#print(min(courses)) # Return min letter in alphabetical order

# print(sum(courses)) # Only works if courses has only numbers

#print(courses.index("Art"))

# print('Art' in courses) # Tests to see if a specific element named "Art" is in courses. this is false
#
nums = [9, 7, 4, 5, 8, 1]
courses = ['History', 'Math', 'Physics', 'CompSci']

# for index, item in enumerate(nums): # index will go first, then item, even if "index" was a different word
#     print(index, item)

# Convert a List to a String (the output is one string), ONLY WORKS WITH STRING IN A LIST, NOT E.G. INT
# courses_str = ' - '.join(courses)
# lis = courses_str.split(' - ')
# print(lis)



#num_str = " - ".join(nums)
#lis = num_str.split(' - ')
#print(lis)

# convert num into string then back into list of numbers

# Join method concatenates a list of strings or iterable objects into a single string
# Split method splits a string into a list

set_1 = {"History", "Math", "Physics", "CompSci"}
set_1.add("Art") # .add only takes one argument
set_1.add("Math")
print(len(set_1)) # Prints 5 bc sets only have unique values, will not add math

# Removes all duplicates from a list by converting to a set, then converting set into a list again, then prints list
list2 = [1, 2, 3, 4, 5, 5]

List_To_Set = set(list2)
list_2 = list(List_To_Set)
print(list_2)

# Prints the intersection of set 4 and set 5
courses_4 = {"History", "Math", "Art", "Physics"}
courses_5 = {"Education", "History", "Chemistry", "Art", "Design"}
print(courses_4.intersection(courses_5)) # AND Gate

# OR GATE
print(courses_4.union(courses_5))

# Courses_4 - Courses_5
print(courses_4.difference(courses_5))

# Creates an empty list (tuple same format)
items = []
items = list()

# DOES NOT CREATE AN EMPTY SET
items = {} # CREATES AN EMPTY DICTIONARY
items = set() # CREATES AN EMPTY SET




