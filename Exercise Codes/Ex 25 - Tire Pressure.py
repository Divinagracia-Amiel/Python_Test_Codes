print("Pressure Check")
rfp = -1
lfp = -1
rbp = -1
lbp = -1
while rfp < 0 or rbp < 0 or lfp < 0 or lbp < 0:
    try:
        rfp = int(input("Input right front tire pressure: "))
        lfp = int(input("Input left front tire pressure: "))
        rbp = int(input("Input right back tire pressure: "))
        lbp = int(input("Input left back tire pressure: "))
    except ValueError:
        print("Please enter a number")
        continue
    if rfp < 0 or rbp < 0 or lfp < 0 or lbp < 0:
        print("Please enter a positive integer")
        continue
if rfp == lfp and rbp == lbp:
    print("Inflation is OK")
else:
    print("Inflation is not OK")
