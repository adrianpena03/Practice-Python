month = int(input("Give me a month as an integer, and I will tell you how many days it has. \n"))

def Days_in_Month(month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month < 1) or (month > 12):
        return "That is not a valid month"
    else:
        return "This month has " + str(days[month]) + " days."

result = Days_in_Month(month)
print(result)

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 == 0 or year % 400 == 0):
        return "This is a leap year."
    else:
        return "This is not a leap year."

year = int(input("Enter a year: "))
result = is_leap_year(year)
print(result)
