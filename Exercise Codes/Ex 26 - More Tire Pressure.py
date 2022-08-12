print("Pressure Check")
rfp = -1
lfp = -1
rbp = -1
lbp = -1
GP = True
while rfp <= 0 or rbp <= 0 or lfp <= 0 or lbp <= 0:
    try:
        rfp = int(input("Input right front tire pressure: "))
        if rfp < 35 or rfp > 45:
            GP = False
            if GP == False:
                print("Warning: Pressure out of range.")
        lfp = int(input("Input left front tire pressure: "))
        if lfp < 35 or lfp > 45:
            GP = False
            if GP == False:
                print("Warning: Pressure out of range.")
        rbp = int(input("Input right back tire pressure: "))
        if rbp < 35 or rbp > 45:
            GP = False
            if GP == False:
                print("Warning: Pressure out of range.")
        lbp = int(input("Input left back tire pressure: "))
        if lbp < 35 or lbp > 45:
            GP = False
            if GP == False:
                print("Warning: Pressure out of range.")
    except ValueError:
        print("Please enter a number")
        continue
    if rfp < 0 or rbp < 0 or lfp < 0 or lbp < 0:
        print("Please enter a positive integer")
        continue
if rfp == lfp and rbp == lbp:
    if rfp < 35 or rfp > 45 or rbp < 35 or rbp > 45:
        print("Inflation is BAD")
    else:
        print("Inflation is OK")
else:
    print("Inflation is BAD")
