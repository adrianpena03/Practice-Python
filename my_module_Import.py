import my_module as mm
# or
# from my_module import find_index as fi, test as t # has to be "from my module" first, then import

list_to_search = [1, 2, 3, 4, 5, 6]
target = 5

print(mm.find_index(list_to_search, target))
