#  n = int(input("Please enter an integer.\n"))

# total = 0
# for i in range (1, 1 + n):
#     if n % 3 != 0:
#         n = n + i
#         print(n)
#         continue


n = int(input("Please enter an integer: "))
result = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    result += i
print("The summation of all numbers that are not a multiple of 3, from 1 to", n, "is", result)