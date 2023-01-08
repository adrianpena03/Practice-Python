
print("Hello, welcome to McDonald's.")

name = input("What is your name? \n")

print("Hello, " + name + ". Thank you for coming in today. \n\n")

menu = "McChicken, Fries, Burger, Nuggets"

print(name + ", the menu is " + menu + ". What would you like?")

order = input()

print("Sounds good " + name + ". We'll have your " + order + " ready for you done in a moment. \n\n\n\n")


def ITE119():
    print("Hello, Professor!")

def name():
    print("My name is %s and i'm %d" % ('Adrian', 18))

def subtraction(num1, num2):
    num3 = num1 - num2
    print (num3)

name() 
ITE119()
subtraction(3, 2)

macbook = {
  "MacbookAir": "13 Inch M1",
  "MacbookPro": "13 Inch M1",
  "MacbookPro2": "14 Inch M1 Pro"
}
macbook["MacbookComp"] = 'iMac'

print(macbook.get("MacbookAir"))
print(macbook)
macbook["MacbookPro2"] = 13

macbook.pop("MacbookPro")
for k,v in macbook.items():
    print(k, '->', v)

print(macbook)

macbook.clear()
print(macbook)



