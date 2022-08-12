print("Pressure Check")
rfp = -1
lfp = -1
rbp = -1
lbp = -1
while rfp < 0 or rbp < 0 or lfp < 0 or lbp < 0:
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
fr_range = rfp - lfp
ba_range = rbp - lbp
if fr_range == 0 and ba_range == 0:
    if rfp < 35 or rfp > 45 or rbp < 35 or rbp > 45:
        print("Inflation is BAD")
    else:
        print("Inflation is OK")
elif rfp >= 35 and rfp <= 45 or rbp >= 35 or rbp <= 45:
    if fr_range <= 3 and fr_range >= -3:
        print("Inflation is OK")
    elif fr_range >= 3 or fr_range <= -3:
        print("Inflation is BAD")
    elif ba_range <= 3 and ba_range >= -3:
        print("Inflation is OK")
    elif ba_range >= 3 or ba_range <= -3:
        print("Inflation is BAD")
    
    
    


   
