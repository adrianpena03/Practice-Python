
print("\n\nHello, welcome to McDonald's.")

name = input("What is your name? \n")



if name == "Ben":
    print("You're not welcome here evil Ben. Get out.")
else:
    print("Hello, " + name + ". Thank you for coming in today. \n\n")




menu = "McChickens, Fries, Burgers, Nuggets"

print(name + ", the menu is " + menu + ". What would you like?")




order = input()

price = 8

Quantity = input("How many " + order + " would you like from the menu? ")

FinalPrice = price * int(Quantity)




print("That will be $" + str(FinalPrice))

print("\nSounds good " + name + ". We'll have your " + Quantity + " " + order + " ready for you in a moment. \n\n\n\n")
