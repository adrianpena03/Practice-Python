#Write a program that receives an integer from the user, called n, and prints the first n prime numbers. For example, if the input is 7, the output should be: 2, 3, 5, 7, 11, 13, 17.

# n = int(input("Enter a number: "))

# prime = 2

# while n != 0:
#     for i in range(2, prime):
#         if prime % i == 0:
#             break
#     else:
#         print(prime, end = ", ")
#         n = n - 1
#     prime = prime + 1

# def IsPrime(n):
#     if n == 2:
#         return True
#     for i in range(2, int(n/2)+1):
#         if n % i == 0:
#             return False
#         else:
#             return True
        
# result = IsPrime(n)
# print(result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def RemovePrime(nums):
    new_list = []
    for num in nums:
        is_prime = True
        if num < 3:
            continue
        else:
            for i in range(2, int(num**1/2)+1):
                if num % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                new_list.append(num)
    return new_list

result = RemovePrime(nums)
print(result)