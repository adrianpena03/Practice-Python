# Write a program that returns the multiplication of two numbers, by addition. Will do this one soon

n = int(input("Give me an integer. "))

# the function should return the sum of the integers from 1 to n and that are not a multiple of 4. WIP


def sum(n):
    for i in range(1, n + 1):
        if i % 4 == 0:
            continue
        i = i + 1
        n = i + n
        return(n)

result = sum(n)
print(result)



