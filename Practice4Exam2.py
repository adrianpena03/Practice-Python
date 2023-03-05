# Given a string, return a string where for every character in the original, 
# there are two characters. 
# Closer to difficulty of problem in exam

# def DoubleLetter(word):
#     New_String = ""
#     for i in range (len(word)):
#         index = word[i]
#         New_String = New_String + index * 2
#     return New_String

# result = DoubleLetter("Adrian")

# Write a function called Eight_count(bin) that receives a string consisting of
# only eights and nines as arguments and returns the biggest number of 
# consecutive eights in the string

bin = "88899988999888888"

def Eight_Count(bin):
    count = 0
    biggest = 0
    for i in bin:
        if i == "8":
            count += 1
        else:
            if count > biggest:
                biggest = count
            count = 0
        if count > biggest:
            biggest = count
    return biggest            

result = Eight_Count(bin)
print(result)

# def eight_count(bin):
#      cons = 0
#      biggest = 0
#      for eights in bin:
#           if eights == "8":
#                cons = cons + 1
#           else:
#                if cons >= biggest:
#                     biggest = cons
#                     cons = 0
#           if cons >= biggest:
#                biggest = cons
#      return biggest

# result = eight_count(bin)
# print(result)

#----------------------------------------
