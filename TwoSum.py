num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def twoSum(num):
    t = 13
    i = 0
    j = 0
    for i in num:
        for j in num:
            if num[i]-1 + num[j]-1 == t:
                return i, j
    print("Not Found.")
    return "No Number Found"

twoSum(num)
