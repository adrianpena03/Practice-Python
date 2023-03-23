# Key: Can be string, Integer, Float, Tuple
# Value: Anything else can be value

# student = {"a":1, "b":3, "c":5} # - Simple Dictionary
student = {
        ("Hi", "You"): 1, 
          "name": 2, 
          "age": 3, 
          }

# print(student["name"]) # - Gets value of key
# print(student.get("name")) # - Another way to get value of key. **Will not return error if key doesn't exist, will return "None"**

student["name"] = "Oliver" # - Replaces value of key, can be any new data type.
student["phone"] = "555-555-55555" # - This adds a new key value pair if it doesn't already exist
print(student)

# del student["phone"] # - Delete a key in dictionary. RETURNS 
# student.pop["age"] # - Another way to delete a key in a dictionary. RETURNS the value associated with the key that was removed

# print(student.keys()) # - Returns all keys from dictionary
# print(student.values()) # - Returns all values from dictionary
# print(student.items()) # - Returns both keys and values in a TUPLE

# for i in student:
#     print(i)

# for i in student.keys():
#     print(i)
# These functions prints out only the keys, NOT values

# for i in student.values():
#    print(i)
# Returns values, NOT keys

# for i in student.items():
#   print(item)
# Returns both key and value

# for key, value in student.items():
#   print(key, value)
# prints key and value also, but it's separate



