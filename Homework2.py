a = int(input("Please enter an integer. \n"))

if a > 0:
    if a % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if a % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
