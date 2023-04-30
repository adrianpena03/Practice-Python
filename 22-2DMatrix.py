# Introduction: A magic square is a 2D matrix composed of n^2 integers where 
# n is the length of one row or column. In a magic square each row, 
# each column, and the two diagonals must sum to the same value.

# Problem: Given a 2D matrix, your program must determine 
# if the square is magic or not magic. It will print "magic" or 
# "non magic" accordingly.
# Input: Your program will first take an input n, representing 
# the length of one row of the matrix from the user. It will then 
# take n lines of input containing n integers separated by spaces from the user.

# Input:
# 3
# 2 7 6
# 9 5 1
# 4 3 8
# Output: "magic"

# Input:
# 4
# 16 2 3 13
# 5 11 10 8
# 9 7 6 12
# 4 14 15 1
# Output: "magic"

# Input:
# 4
# 12 3 4 5
# 5 67 8 9
# 102 3 4 6
# 34 2 89 0
# Output: "not magic"

#--------------------------
n = int(input("Enter the length of one row of the matrix: "))

# initialize the matrix
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# calculate the sum of the first row
sum_first_row = sum(matrix[0])

# check if each row, column, and diagonal sums to the same value
for i in range(n):
    # check rows
    if sum(matrix[i]) != sum_first_row:
        print("not magic")
        exit()
    # check columns
    if sum(matrix[j][i] for j in range(n)) != sum_first_row:
        print("not magic")
        exit()
    # check diagonal from top left to bottom right
    if sum(matrix[i][i] for i in range(n)) != sum_first_row:
        print("not magic")
        exit()
    # check diagonal from top right to bottom left
    if sum(matrix[i][n-i-1] for i in range(n)) != sum_first_row:
        print("not magic")
        exit()

# if all checks pass, the square is magic
print("magic")
