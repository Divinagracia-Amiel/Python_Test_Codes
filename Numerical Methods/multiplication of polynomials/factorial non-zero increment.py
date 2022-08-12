power = int(input("What is the power of the factorial? "))
counter = 0
C_list = [1, -3]
MP = [1, -4]
C_count = 0
row1 = []
row2 = []
#for i in range(1, power):
    #counter += 2 * power
    #power -= 1
#print(f"{counter}")

for a in range(1, power):
    for b in range(0, 2):
        C = C_list[b]
        for c in range(0, len(MP)):
            MP_constant = C * MP[c]
            if C_count == 0:
                row1.append(MP_constant)
                print(f"{row1}")
            elif C_count == 1:
                row2.append(MP_constant)
                print(f"{row2}")
        if b == 1:
            MP = []
            MP.append(row1[0])
            for d in range(1, len(row1)):
                MP.append(row1[d] + row2[d-1])
            MP.append(row2[len(row2)-1])
        C_count += 1
    row1 = []
    row2 = []
    C_update = C_list[1] + 1
    C_list[1] = C_update
    C_count = 0
print(f"{MP}")