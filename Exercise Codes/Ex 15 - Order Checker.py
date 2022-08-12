cont = "y"
while cont == "y":
    prBolt = 5
    prNut = 3
    prWash = 1
    QBolt = -1
    QNut = -1
    QWash = -1
    cont = False
    while QBolt < 0 or QNut < 0 or QWash < 0:
        try:
            QBolt = int(input("Input the number of bolts: "))
            QNut = int(input("Input the number of Nuts: "))
            QWash = int(input("Input the number of Washers: "))
        except ValueError:
            print("Please input an integer")
            continue
        if QBolt < 0 or QNut < 0 or QWash < 0:
            print("Please write a positive integer")
            continue
    choice = True
    Cost_Bolt = QBolt * prBolt
    Cost_Nut = QNut * prNut
    Cost_Wash = QWash * prWash
    if QBolt <= QNut: 
        print("Order is OK.\n",
              f"Bolts: {QBolt} Bolt/s\n",
              f"Nuts: {QNut} Nut/s \n",
              f"Washers: {QWash} Washer/s \n")
        break
    if QBolt > QNut:
        print("Check the Order.\n",
              f"Bolts: {QBolt} Bolt/s\n",
              f"Nuts: {QNut} Nut/s \n",
              f"Washers: {QWash} Washer/s \n",
              "The quantity of bolts should not be more than that of the nuts \n")
        while cont != choice:
            cont = input("Would you like to re-order? Y/N ")
            if cont.lower().strip() == "y" or cont.lower().strip() == "n":
                break
            elif cont != choice:
                print("Please enter an letter that is Y or N in upper/lowercase")
                continue
    if cont.lower().strip() == "y":
        continue
    if cont.lower().strip() == "n":
        break
Total = Cost_Bolt + Cost_Nut + Cost_Wash
print(f"Number of Bolts:\n{QBolt} Bolt/s\n",
      f"Number of Nuts:\n{QNut} Nut/s\n",
      f"Number of Washers:\n{QWash} Washer/s\n",
      f"\nTotal Cost: {Total}")

    
    
    
    