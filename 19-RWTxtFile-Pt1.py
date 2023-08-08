# Prepare a txt file that has five lines with three words on each line, 
# separated with a space. Write a program that reads the txt file and 
# makes three lists out of it and prints the three lists. The elements of 
# the first list are the first word on each line. The elements of the second 
# list are the second word on each line. The elements of the third list are the 
# third word on each line. Each list has five elements. Make sure that there 
# are no new line characters in the elements.

list_1 = []
list_2 = []
list_3 = []

with open('19File.txt', 'r') as file:
    for line in file:
        words = line.split()
        if len(words) > 0:
            list_1.append(words[0])
        if len(words) > 1:
            list_2.append(words[1])
        if len(words) > 2:
            list_3.append(words[2])

print("The first list is:", list_1)
print("The second list is:", list_2)
print("The third list is:", list_3)


