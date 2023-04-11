# Write a program that defines dict={'name': 'John', 'expertise': 'Math'}, 
# then asks for an input from the user and prints True if the user input 
# exists among the values of the dictionary and False if it does not. 

my_dict = {'name': 'John', 'expertise': 'Math'}

user_input = input("Enter a value: ")

if user_input in my_dict.values():
    print(True)
else:
    print (False)
