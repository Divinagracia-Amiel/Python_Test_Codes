
age = float(input("What is your age?"))
if age < 18:
    print("bruh u a minor tho, no entering")
    quit()
elif age > 18:
    print("bruh u may enter with caution")

Qtty = int(input("Please state how many tickets would you like to buy"))

if Qtty > 0:
    Price = float(input("What is the price of the ticket that you would like to buy?"))
    Cost = Qtty * Price
    print("The total cost would be $%.2f. Thank you for choosing our services" %(Cost))
    quit()
if Qtty == 0:
    Cost = 0
    print("See you next time!")
    quit()

        