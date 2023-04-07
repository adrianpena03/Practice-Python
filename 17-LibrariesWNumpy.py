# Write a program to delete the second column from the following array and 
# insert the following new column in its place, and print the result.

# original_array = numpy.array(
# [34 43 73]
# [82 22 12]
# [53 94 66]])
# new_column = numpy.array([[10,10,10]])
# After insertion, your array should look like:
# [[34 10 73]
# [82 10 12]
# [53 10 66]]

import numpy

original_array = numpy.array(
    [[34, 43, 73],
    [82, 22, 12],
    [53, 94, 66]]
)

# Delete the second column
modified_array = numpy.delete(original_array, 1, axis=1)

# Insert new column at the second position
new_column = numpy.array([[10, 10, 10]])
modified_array = numpy.insert(modified_array, 1, new_column, axis=1)

print(modified_array)
