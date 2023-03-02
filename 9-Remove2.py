# Write a Python function to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead an empty string. For instance, it should return unrn for unicorn. 
# Call that function and print its output.



def First_Last(word):
    if len(word) <= 2:
        return " "
    else:
        return word[:2] + word[-2:]

# Test
word = "unicorn"
result = First_Last(word)
print(result)