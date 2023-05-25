# Prepare a txt file that has five sep_lines with three words on each sep_line, 
# separated with a space. Write a program that reads the txt file and 
# makes three lists out of it and prints the three lists. The elements of 
# the first list are the first word on each sep_line. The elements of the second 
# list are the second word on each sep_line. The elements of the third list are the 
# third word on each sep_line. Each list has five elements. Make sure that there 
# are no new sep_line characters in the elements.

list_1 = []
list_2 = []
list_3 = []

with open('19File.txt', 'r') as file:
    for ln in file:
        sep_line = ln.split()
        if len(sep_line) > 0:
            list_1.append(sep_line[0])
        if len(sep_line) > 1:
            list_2.append(sep_line[1])
        if len(sep_line) > 2:
            list_3.append(sep_line[2])

print("The first list is:", list_1)
print("The second list is:", list_2)
print("The third list is:", list_3)
