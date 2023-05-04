# Approach 1:
f = open("Exfile.txt", "r")
# Do something
f.close()

# Approach 2
with open("Exfile.txt", "r") as f:
    pass
    # Do something with the file
# if you start aa new line here, without indentation, it will close the file

# r: read
# w: overwriting?
# r+: If file exists, it will not delete what is already in file. read and write (return error if file doesn't exist)
# w+: (if file doesn't exist, will create it for you. If does exist, will delete what is in file.) 
# a: append, opens file fo r purpose of writing, ONLY ADDS ONTO. (If file doesn't exist, it will add. Will not return error if doesn't error)
# a+: also allows you to read from file

with open("Exfile.txt") as f:
    # print(f.name)
    # var = f.read() # reads entire content of file into one string variable. Data type is STR
    # whole_content = f.read()
    # print (whole_content)
    list_of_lines = f.readlines() # Reads a whole file and puts it into a single line as a LIST
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].strip("\n")
    print(list_of_lines)

with open("Exfile.txt", "r") as f:
    first_line = f.readline() # returns only one line of the file as a string
    print(first_line) # prints first line
    second_line = f.readline()
    print(second_line) # prints second line

with open("Exfile.txt", "r") as f:
    read_lines = f.readline()
    for ln in f:
        print(ln) # prints all lines
    
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

try:
    f = open("Exfile.xt") # Can only have 1 try
except:
    print("Sorry, could not open the file.") # Can have 1 or more except clauses

try:
    f = open("Exfile.xt")
except FileNotFoundError:
    print("Sorry, could not open the file.")
except NameError as ne: # nickname
    print(ne)
except Exception:
    print("Somethng went wrong.") # ONLY 1 of except blocks will be run. THe first one that catches error
else:
    print("else block was triggered...") # 0 or 1 else clause. Will only run if no exceptions were thrown.
finally: # Finally will always be executed, error or not.
    print("Finally was triggered.") # 0 or 1 finally clause

# def function(n):
#     if n == 1:
#         return 2
#     else:
#         return 1400 * function(n - 1)

# for i in range(1, 3):
#     print(function(i))