# Write a program that returns the multiplication of two numbers, by addition

n = int(input("Enter an integer, and I wil tell you if it is prime or not. "))


for i in range(2, n+1):
    if n % i == 0:
        print("The integer you gave is not a prime number.")
        break
    else:
        print("The integer you gave is a prime number.")
        break
        


# Prime is a number greater than one that is divisible by only 1 and itself to get a remainder of 0
