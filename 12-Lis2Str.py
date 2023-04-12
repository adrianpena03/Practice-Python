# Homework 12 about Lists, Tuples, and Sets: Write a function that receives a 
# list of integers as its argument. The function should join individual elements 
# of this list of integers to create a string. Inside the string, the elements 
# should be separated using a comma. Then print the string. 
# For instance, if you call the function and pass [1, 2, 3], the returned string should be "1,2,3". 
# Please note that there is no space around the comma in the string.
# Please note that the join function only operates on lists whose elements are string. 
# Since your list includes integers in this case, you need to take an extra step to make it possible to use the join function.

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def Lis2Str(lis):
    lis_string = [str(num) for num in lis]
    str_join = ",".join(lis_string)
    return str_join

print(Lis2Str(lis))

word = "Backwards"
def str_lis(word):
    new_str = word.split(', ')
    str_lis = [list(char) for char in word]
    return str_lis

print(str_lis(word))