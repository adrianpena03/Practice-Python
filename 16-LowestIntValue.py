# Write a function that receives a dictionary as input
# and prints out the key for the minimum value among the dictionary values. 
# Call that function and print its output. 
# You can test your function with {'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19} 
# and it should print out Physics.

dict = {
        'Math': 25, 
        'History': 20, 
        'Physics': 18, 
        'Geography': 19
        } 

min_value = min(dict.values())
print(min_value)

