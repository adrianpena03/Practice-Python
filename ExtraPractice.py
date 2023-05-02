
# Problem 1: Return true of one of them is 10, or the sum of a + b is 10
def ifTen(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False

a = 6
b = 7
#print(ifTen(a, b))

# Problem 2: Given integers a and b, return True if either one is 6. Or if their sum or difference is 6.
# The difference is always 6. 7 - 1 = 6 and 1 - 7 = 6
def Difference6(a, b):
    if a == 6 or b == 6:
        return True
    elif a + b == 6:
        return True
    elif a - b == 6:
        return True
    elif b - a == -6:
        return True
    else:
        return False

# print(Difference6(a, b))

# Problem 3: Given a non-empty string and an int n, return a new string where the
# character at index n has been removed.

str = "Adrian"

n = 4

def RemoveNIndex(str, n):
    new_str = ''
    for index, value in enumerate(str):
        if n == index:
            continue
        new_str = new_str + value
    return new_str
 
#print(RemoveNIndex(str, n))

# Problem 4: Given a list of ints, return True if the list contains a 2 next to a 2 somewhere

nums = [1, 2, 2, 3, 4, 5, 6]

def ConsTwo(nums):
    cons = 0
    for num in nums:
        if num == 2:
            cons = cons + 1
        else:
            cons = 0
        if cons == 2:
            return True
    return False

# or 

def has_two_adjacent(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 2:
            return True
    return False


print(ConsTwo(nums))


# Problem 5: Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences



# Problem 6: Flatten a list, write a function that takes a list and flattens it into a one-dimensional list.
