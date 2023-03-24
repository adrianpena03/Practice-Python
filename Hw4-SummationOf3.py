n = int(input("Please enter an integer: "))

result = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    result = result + i

print(result)

# n = int(input("Please enter an integer: "))

# def summation(result):
#     result = 0
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             continue
#         result = result + i
#     return(result)

# r = summation(n)
# print(r)
