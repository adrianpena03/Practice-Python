# Write a python program to get a string as input from the user and print the third character from the end. 
# For instance, it should return "o" for unicorn.

n = input("Give me a word. ")

def Print_Third(n):
    return (n[-3])

result = Print_Third(n)
print(result)

