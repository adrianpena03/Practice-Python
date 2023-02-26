# Write a python program to get a string as input from the user and print the third character from the end. 
# For instance, it should return "o" for unicorn.

word = "Adrian"

def Print_Third(word):
    return (word[len(word)-3])

result = Print_Third(word)
print(result)
