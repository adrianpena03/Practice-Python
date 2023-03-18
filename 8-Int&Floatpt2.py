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

num = 1
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if num % i == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")