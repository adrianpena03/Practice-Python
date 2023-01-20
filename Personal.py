
print("\n\nHello, welcome to McDonald's.")

name = input("What is your name? \n")



if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here evil Ben. Get out.")
        exit()
    else:
        print("Oh, so you're one of the good Bens. Come on in!")
else:
    print("Hello, " + name + ". Thank you for coming in today. \n\n")




#menu = "McChickens, Fries, Burgers, Nuggets"

#print(name + ", the menu is " + menu + ". What would you like?")


if order == "McChicken":
    


#order = input()

if order == "McChicken":
    price = 3
elif order == "Fries":
    price = 2
elif order == "Burger":
    price = 5
elif order == "Nuggets":
    price = 1
else:
    print("Sorry, we don't have that here.")
    price = 0

#Quantity = input("How many " + order + " would you like from the menu? ")

#FinalPrice = price * int(Quantity)




print("That will be $" + str(FinalPrice))

print("\nSounds good " + name + ". We'll have your " + Quantity + " " + order + " ready for you in a moment. \n\n\n\n")
