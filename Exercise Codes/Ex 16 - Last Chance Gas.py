print("Alert: There are no other gas stations for 200 miles")
Cap = -1
Gauge = -1
MpG = -1
while Cap < 0 or Gauge < 0 or MpG < 0:
    try:
        Cap = int(input("What is the gas capacity of the car(in gallons)?"))
        Gauge = int(input("How much gas is left based on the gauge reading in the car(in percentage)?"))
        MpG = int(input("How much gas does the vehicle use(in miles per gallon)"))
    except ValueError:
        print("Please input an integer")
        continue
    if Cap < 0 or Gauge < 0 or MpG < 0:
        print("Please write a positive integer")
        continue
    if Gauge > 100 and Gauge <= 0:
        print("Please pick a number from 0 to 100 only")
        continue
    
Rem = Cap * (Gauge/100)
Dist = Rem * MpG
print(f"Tank capacity:\n{Cap} Gallons\n",
      f"Gauge reading:\n{Gauge}%\n",
      f"Miles per gallon:\n{MpG}")
if Dist < 200:
    print("Get Gas!")
else:
    print("Safe to Proceed")
    
    
    
    


