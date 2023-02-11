#Homework 7 about Integers and Floats: Write a program that receives an integer, greater than or equal to 2, from the user and prints whether that number is odd or even.

a = int(input("Please give me a number that is greater or equal to 2. "))

def even_or_odd(a):
    if a >= 2:
        if a % 2 == 0:
            return(str(a) + " is even")
        else:
            return(str(a) + " is odd")
    else:
        return("Number is not greater than or equal to 2")

result = even_or_odd(a)
print(result)
