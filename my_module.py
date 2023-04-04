print("Imported My Module...")

test = "Test String"

# Find the index of a value in a list
def find_index(list_to_search, target):
    for index, value in enumerate(list_to_search):
        if value == target:
            return index

    return -1 # If the value does not exist in the list, return -1

def func1():
    print("Hello!")