# Write a program that returns the multiplication of two numbers, by addition

n = int(input("Enter an integer, and I wil tell you if it is prime or not. "))

i = 2

while i < n:
    if n % i == 0:
        print("Integer is not prime.")   
        break 
    i += 1
    
    
    
    if i == n - 1:
        print("Prime")
        break

# for i in range(3, n+1):
#     print(i)
#     if n % i == 0:
#         print("The integer you gave is not a prime number.")
#         break
#     else:
#         print("The integer you gave is a prime number.")
#         break
        


# Prime is a number greater than one that is divisible by only 1 and itself to get a remainder of 0
