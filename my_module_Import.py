# import my_module as mm
# or
# from my_module import find_index as fi, test as t # has to be "from my module" first, then import

from my_module import RemovePrime as RP, find_index as fi

list_to_search = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

print(fi(list_to_search, target))

print(RP(list_to_search))