# H 12 about Lists, Tuples, and Sets: Write a function that receives a 
# list of integers as its argument. The function should join individual elements 
# of this list of integers to create a string. Inside the string, the elements 
# should be separated using a comma. Then print the string. 
# For instance, if you call the function and pass [1, 2, 3], the returned string should be "1,2,3". 
# Please note that there is no space around the comma in the string.
# Please note that the join function only operates on lists whose elements are string. 
# Since your list includes integers in this case, you need to take an extra step to make it possible to use the join function.

nums = [1, 2, 3, 4, 5]
def LisToStr(nums):
    new_str = [str(num) for num in nums]
    str_join = ','.join(new_str)
    return str_join

print(LisToStr(nums))

nums = "123456"

# Now backwards
def StrToLis(nums):
    Separate = [list(i) for i in nums]
    return Separate

print(StrToLis(nums))

#-----------------------------------------
# H 13 about Lists, Tuples, and Sets: Write a function that receives
# a list of integers and prints out that list after removing prime numbers from the list.
# Test your program with multiple lists of numbers and make sure it works properly. 
# For instance, if the input is [1, 2, 3, 4, 5, 6, 7], it should print [1, 4, 6] or [4, 6]. 
# However you decide to treat 1 is okay.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def RemovePrime(nums):
    new_list = []
    for num in nums:
        if num <= 3:
            continue
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    new_list.append(num)
                    break
                else:
                    continue
    return new_list

print(RemovePrime(nums))



#---------------------------------------------------
# H 14: Define list_1 = ['Ten', 'Twenty', 'Thirty'] and list_2 = [10, 20, 30], then write a program 
# that uses a for loop to create a dictionary called dict whose keys are items from list_1
# and whose values are items from list_2 and then prints the dict. 





#----------------------------------------------------
# H 15: Write a program that defines dict={'name': 'John', 'expertise': 'Math'}, 
# then asks for an input from the user and prints True if the user input 
# exists among the values of the dictionary and False if it does not. 







#-----------------------------------------------------
# H 16: Write a function that receives a dictionary as input
# and prints out the key for the minimum value among the dictionary values. 
# Call that function and print its output. 
# You can test your function with {'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19} 
# and it should print out Physics.




#-------------------------------------------------------