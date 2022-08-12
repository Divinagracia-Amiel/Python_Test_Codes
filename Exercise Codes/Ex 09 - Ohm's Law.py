Volt = False
Res = False
while Volt == False:
    try:
        Volt = int(input("What is the voltage of the battery"))
    except ValueError:
        print("Please enter an integer\n")
        continue
    break
while Res == False:
    try:
        Res = int(input("What is the collective resistance in the device"))
    except ValueError:
        print("Please enter an integer\n")
        continue
    if Res == 0:
        print("Division by zero is undefined, please try again.\n")
        continue
    break
I = (Volt + 0.0) / Res
print(f"The current in the device is {I} amperes")



