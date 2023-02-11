# Camping Trip


# Python List: Ordered and changeable collection of data objects. Can contain mixture of objects (unlike array).
camping_list = ["tent", "sleeping bags", "water", "rasberry pi", "coffee", "knife", "ethernet cable", "flash drive", "hair oil", "marshmallows"]

camp_site = ["crystal Lake", 404, 89.3, True]

#me = camping_list[3]
#print(me)

#you = camping_list[-2]
#print(you)

#print(camping_list)

# Method: Function that is available for a given object because of the object's type
camping_list.append("toilet paper")

camping_list.extend(["bidet", "lighter"])

camping_list = camping_list + ["bow", "axe"]

camping_list.insert(0, "arrow")

camping_list.insert(-1, "pan")



camping_list.remove("tent")

camping_list.pop(9)

print(camping_list.pop(8))

print(camping_list)

