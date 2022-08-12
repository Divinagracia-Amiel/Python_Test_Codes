print("You must weigh within 30 pounds to 250 pounds to enter the Pie Eating Contest")
weight = -1
while weight < 0:
    try:
        weight = float(input("What is your weight in pounds?"))
    except ValueError:
        print("Please input a number")
        continue
    if weight < 0:
        print("Please input positive numbers")
        continue
if weight < 220 or weight > 280:
    print("Sorry, you are not allowed to join this contest.")
else:
    print("Congratulations, you are allowed to join this contest.")
    
    