# Define list_1 = ['Ten', 'Twenty', 'Thirty'] and list_2 = [10, 20, 30], then write a program 
# that uses a for loop to create a dictionary called dict whose keys are items from list_1
# and whose values are items from list_2 and then prints the dict. 

list_1 = ['Ten', 'Twenty', 'Thirty']
list_2 = [10, 20, 30]

my_dict = {}

for i in range(len(list_1)):
    key = list_1[i]
    value = list_2[i]
    my_dict[key] = value


# Testing Code
print(my_dict)

