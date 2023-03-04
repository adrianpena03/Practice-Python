# Write a function that receives a tuple as input. The tuple might include duplicates. 
# Convert the tuple to a set which will remove duplicates automatically. 
# Then convert the set to a list. Then sort the list. 
# Then create a new list that includes the items in the previous list, each one duplicated as many times as its index. 
# For instance, the first item in the list would appear only once in the new list, 
   # the second item in the list would appear two times in the list, etc. 
# Then it prints the new list and returns the new list. For instance, if the input is ('b', 'a', 'c', 'a', 'c'), 
# the output should be ['a', 'b', 'b', 'c', 'c', 'c']. If the input is (8, 5, 6, 6), the output should be [5, 6, 6, 8, 8, 8].

tup = (1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8)

tup_set = set(tup)

print(tup_set)