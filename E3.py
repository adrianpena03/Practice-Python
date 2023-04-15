
def Factorial(n):
    dict = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
        dict[i] = factorial
    return dict


n = 5
print(Factorial(n))

#def Cubed(n):