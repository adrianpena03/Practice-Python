

def CalculateBMI(weight, height, name = "James"):
    BMI = weight/(height) ** 2
    if BMI >= 22:
        return("BMI is greater than 22.")
    else:
        return("BMI is less than 22.")

result = CalculateBMI(60, 1.7, "James")

print(result)
