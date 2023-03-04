# Write a program that returns the multiplication of two numbers, by addition. Will do this one soon

f = int(input("Give me an integer. "))
s = int(input("Give me another integer. "))

def Multiply_By_Adding(f, s):
    multiply = 0
    for i in range(s):
        multiply = multiply + f
        print(multiply)
    return multiply

result = Multiply_By_Adding(f, s)
print(result)

