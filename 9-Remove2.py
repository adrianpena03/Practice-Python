# Write a Python function to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead an empty string. For instance, it should return unrn for unicorn. 
# Call that function and print its output.

# message = "Hello World"

# print('message[len(message)-1: ', message[len(message)-1])
# print(message.find("Hello")) # Prints 0 (ig for index 0)

word = "unicorn"
def First_Last(word):
    if len(word) < 2:
        return " "
    else:
        new_string = word[0] + word[1] + word[len(word)-2] + word[len(word)-1] 
    return new_string

result = First_Last(word)
print(result)