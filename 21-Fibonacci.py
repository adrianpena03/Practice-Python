# The Fibonacci Sequence is a series of numbers. 
# The first two numbers are 0 and 1. The next number is found by 
# adding up the two numbers before it. For example, 0, 1, 1, 2, 3, 5, 
# 8, 13, 21. The next number in this series is 13+21 = 34. 
# Write a program that receives an integer from the user, 
# called n, and prints out Fibonacci series up to n terms. 
# For example, if the user types 5, your program should print out 
# 0, 1, 1, 2, 3.

n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# initialize the first two terms
value_1 = 0
value_2 = 1

# print the first n terms of the sequence
for i in range(n):
    print(value_1, end=" ")
    next_value = value_1 + value_2
    value_1 = value_2
    value_2 = next_value
