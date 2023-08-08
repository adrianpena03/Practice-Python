# Make a txt file and write 10 lines of text in it, anything.
# Read the file in Python and write a new txt file using your code 
# that includes every other line in the first text file. Therefore, 
# the new txt file has five lines which are line 1, line 3, line 5, 
# line 7, and line 9 in the first txt file.

with open("20File.txt", "r") as f:
    with open("20New.txt", "w") as t:
        count = 0
        for ln in f:
            count += 1
            if count % 2 != 0:
                t.write(ln)

# Testing Code
with open("20New.txt", "r") as t:
    contents = t.read()
    print(contents)
