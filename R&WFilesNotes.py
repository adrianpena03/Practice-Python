# # Approach 1:
# f = open("Exfile.txt", "r")
# # Do something
# f.close()

# Approach 2
# with open("Exfile.txt", "r") as f:
#     pass
    # Do something with the file
#if you start aa new line here, without indentation, it will close the file

# r: read?
# w: overwriting?
# r+: If file exists, it will not delete what is already in file. read and write (return error if file doesn't exist)
# w+: (if file doesn't exist, will create it for you. If does exist, will delete what is in file.) 
# a: append, opens file for purpose of writing, ONLY ADDS ONTO. (If file doesn't exist, it will add. Will not return error if doesn't error)
# a+: also allows you to read from file

# with open("Exfile.txt") as f:
#     # print(f.name)
#     # var = f.read() # reads entire content of file into one string variable. Data type is STR
#     # whole_content = f.read()
#     # print (whole_content)
#     list_of_Lines = f.readlines() # Reads a whole line, it is a list
#     for i in range(len(list_of_Lines)):
#         list_of_lines[i] = list_of_lines[i].rstrip("\n")
#     print(var)

# with open("Exfile.txt", "r") as f:
#     first_line = f.readline() # returns only one line of the file as a string
#     print(first_line) # prints first line
#     second_line = f.readline()
#     print(second_line) # prints second line

# with open("Exfile.txt", "r") as f:
#     read_lines = f.readline()
#     for ln in f:
#         print(ln) # prints all lines
    
# with open("Exfile.txt", "r") as f:
#     f.write("Hello you!") # Writes to file
#     f.write("Goodbye") # Writes after previous write, no spaces

with open("Exfile.txt", "r") as r_f:
    with open("Exfile1.txt", "w") as w_f:
        for ln in r_f:
            w_f.write(ln)

        # Second Approach
        ln = r_f.readline()
        while len(ln) > 0:
            w_f.write(ln)
            ln = r_f.readline