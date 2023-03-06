# Me-21 = "Hi" - Not allowed bc dash
# 2Em = 'Hi' - Not allowed bc starts w number

message = 'John\'s Book'
message = 'John\s Book'
message = "John\'s Book"
print(message)
# escape character python, counts as 1

message = "John\\\s Book"
message = "Hello World"
message = "John\\\\s Book"
print(message)

message = "Hello World"
print('len(message): ', len(message))

print('message[0]', message[0]) # indexing uses brackets

#print(message[len(message)]) # - QUESTION ON EXAM

print('message[len(message)-1: ', message[len(message)-1])

print("Message Last Letter: ", message[1:6:7])
print('message[0:0]: ', message[:5]) # prints nothing

print('message[0:0]: ', message[1:6:2]) # 2 means take 2 steps

print('message[0:0]: ', message[2::-1])
print('message[0:0]: ', message[::-1])

message = "Hello World"
print(message.count('hello')) # Will not get error, will be 0 if doesn't exist
print(message.count("Hello")) # Prints 1
print(message.find("Hello")) # Prints 0 (for index 0?)


# Given a string name, e.g. 'Bob', return a greeting of the form 'Hello Bob!'.

def Greeting(name):
    return "Hello " + name + "!"

# P2: Given a string and a non-negative int n, return a larger string that is n # copies of the original string

def Larger(string, n):
        return string * n


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 characters
# or whatever is there if the string is less tha length 3. Return the n copies of the front.

def func3(word, n):
    front = " "
    if len(word) < 3:
        front = word
    else:
        front = word[0:3]
    return front * n

# Given a string, return a string where for every character in the original, there are two characters. Closer to difficulty of problem in exam
def DoubleLetter(str):
    new_string = " "
    for i in str:
        new_string += i*2
    return new_string

# OR

def Double_Char(str):
    return " ".join([c * 2 for c in str])





# Write a function called Eight_count(bin) that receives a string consisting of only eights and nines as arguments
# and returns the biggest number of consecutive eights in the string

bin = [9, 8,8,8,8,8,9, 8, 8, 8, 8, 9]

def eight_count(bin):
     cons = 0
     biggest = 0
     for eights in bin:
          if eights == 8:
               cons = cons + 1
          else:
               if cons >= biggest:
                    biggest = cons
                    cons = 0
          if cons >= biggest:
               biggest = cons
     return biggest

result = eight_count(bin)
print(result)

# def summation():
#     sum = 0
#     nums = [1, 2, 3, 4, 5]
#     for i in nums:   
#         sum = sum + i
#     return sum

# print(summation())

      
# def Double_Char():
#     name = "Adrian"
#     new_string = " "
#     for i in name:
#         new_string = new_string + i * 2
#     return new_string

# print(Double_Char())
# word = "Adrian"

# def String_Split(word):
#      ns = " "
#      for letter in word:
#           ns = ns + letter + "$"
#      return ns

# result = String_Split(word)
# print(result)