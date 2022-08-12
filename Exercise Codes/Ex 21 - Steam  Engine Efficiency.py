Tair = -1
Tsteam = -1
print("This is a Steam Engine Efficiency Calculator\nnote*\nStandard Air Temperature: 300K\nBoiling Point of Water: 373K")
while Tsteam <= 0 or Tair < 0:
    try:
        Tair = float(input("What is the temperature of the air?(in kelvin)"))
        Tsteam = float(input("What is the temperature of the steam?(in kelvin)"))
    except ValueError:
        print("Please input a number")
        continue
    if Tsteam == 0 and Tair == 0:
        print("Indeterminate Form detected. Try again.")
        continue
    if Tsteam == 0:
        print("Undefined. Please try again")
    if Tsteam < 0 or Tair < 0:
        print("There is no negative value of kelvin. Please try again.")
        continue
efficiency = 1 - (Tair / Tsteam)
Per_eff = efficiency * 100
if Tsteam < 373:
    efficiency = 0
    print("Since there is no steam, The efficiency of the steam engine is 0")
else:
    print("The efficiency of the steam engine is %.3f or %.3f in percentage" %(efficiency, Per_eff))

