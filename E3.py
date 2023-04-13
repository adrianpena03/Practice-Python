
def Factorial(n):
    dict = {}
    user_input = n
    factorial = 1
    for i in range(1, user_input + 1):
        factorial = factorial * i
        key = i
        dict[key] = factorial
    return dict


n = 10
print(Factorial(n))