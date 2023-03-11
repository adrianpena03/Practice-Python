#Write a program that receives an integer from the user, called n, and prints the first n prime numbers. For example, if the input is 7, the output should be: 2, 3, 5, 7, 11, 13, 17.

n = int(input("Enter a number: "))

prime = 2

while n != 0:
    for i in range(2, prime):
        if prime % i == 0:
            break
    else:
        print(prime, end = ", ")
        n = n - 1
    prime = prime + 1

#just do in a for loop or while loop. if num%i == 0, 
# then ‘not prime’, move on to next. If prime, add/append 
# to list or print.