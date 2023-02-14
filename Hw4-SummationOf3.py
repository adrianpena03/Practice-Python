n = int(input("Please enter an integer: "))

result = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    result = result + i

print("The summation of all numbers for", n, "that are not a multiple of 3, is", result)
