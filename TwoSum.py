num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 10

def twoSum(target, num):
    for i in num:
        for j in num:
            if num[i] + num[j] == target:
                return i, j
            return "Not Found"

print(twoSum(target, num))


# WIP