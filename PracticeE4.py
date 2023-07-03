# Prepare a txt file that has five lines with three words on each line, 
# separated with a space. Write a program that reads the txt file and 
# makes three lists out of it and prints the three lists. The elements of 
# the first list are the first word on each line. The elements of the second 
# list are the second word on each line. The elements of the third list are the 
# third word on each line. Each list has five elements. Make sure that there 
# are no new line characters in the elements.

lis1 = []
lis2 = []
lis3 = []

with open ("19File.txt", "r") as f:
    for ln in f:
        words = ln.split()
        if len(words) > 0:
            lis1.append(words[0])
        if len(words) > 1:
            lis2.append(words[1])
        if len(words) > 2:
            lis3.append(words[2])

# print("List 1 contains:", lis1)
# print("List 2 contains:", lis2)
# print("List 3 contains:", lis3)

# ----------------------------------------
# Make a txt file and write 10 lines of text in it, anything.
# Read the file in Python and write a new txt file using your code 
# that includes every other line in the first text file. Therefore, 
# the new txt file has five lines which are line 1, line 3, line 5, 
# line 7, and line 9 in the first txt file.

with open ("20File.txt", "r") as r_20:
    with open("20New.txt", "w") as w_20New:
        count = 0
        for ln in r_20:
            count += 1
            if count % 2 != 0:
                w_20New.write(ln)

with open ("20New.txt", "r") as w_20New:
    contents = w_20New.read()
    #print(contents)

# -------------------

# Trying to take a number from a file, then use that number in a function.
# WIP

# n = int(input("Give me a number. "))

# def Summation(n):
#     result = 0
#     for i in range(0, n + 1):
#         if i % 4 == 0:
#             continue
#         result = result + i
#     return result

# print(Summation(n))

# def CreateTxtWn(n):
#     n = int(input("Give me a number. "))
#     with open("PracticeSummation.txt", "w+") as f:
#         f.write(n)

stri = "AABBCCC"
def DoubleChar(stri):
    dict = {}
    counter = 0
    for i in range(len(stri)-1):
        if stri[i] == stri[i + 1]:
            counter = counter + 1
        else:
            counter = 0
        dict[i] = counter
    return dict

print(DoubleChar(stri))

# WIP