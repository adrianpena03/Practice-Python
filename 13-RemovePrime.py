# Homework 13 about Lists, Tuples, and Sets: Write a function that receives
# a list of integers and prints out that list after removing prime numbers from the list.
# Test your program with multiple lists of numbers and make sure it works properly. 
# For instance, if the input is [1, 2, 3, 4, 5, 6, 7], it should print [1, 4, 6] or [4, 6]. 
# However you decide to treat 1 is okay.


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def RemovePrime(nums):
    new_list = []
    for num in nums:
        if num <= 3:
            continue
        else:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    new_list.append(num)
                    break
                else:
                    continue
    return new_list

result = RemovePrime(nums)
print(result)

