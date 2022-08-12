print("10% SALE! ON ALL PURCHASES ABOVE $10.00")
origprice = False
while origprice == False:
    try:
        origprice = int(input("Please enter the amount of purchases in cents: "))
    except ValueError:
        print("Please enter an integer")
        continue
    break
if origprice > 1000:
    disprice = origprice * 0.90
    pricein_D = disprice / 100
    print(f"Discounted price: $%d" %(pricein_D))
else:
    pricein_D = origprice / 100
    print(f"Since it is not above $10.00, The total cost is $%d" %(pricein_D))

