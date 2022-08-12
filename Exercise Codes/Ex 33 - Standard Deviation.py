import math
cyc = False
while cyc == False:
    try:
        cyc = int(input("How many numbers are in the set? "))
    except ValueError:
        print("Please input an integer")
        cyc = False
        continue
    if cyc < 0:
        print("Please input a positive number")
        cyc = False
        continue
count = 1
_sum = 0
_sumsq = 0
while count <= cyc:   
    try:
        add = int(input("Enter an integer "))
    except ValueError:
        print("Enter an integer")
        continue
    _sum = _sum + add
    _sumsq = _sumsq + (add ** 2)
    count = count + 1
ave = _sum / cyc
sq_ave = ave ** 2
_sumsqave = _sumsq / cyc
SD = math.sqrt(_sumsqave - sq_ave)
print(f"The standard deviation of the set is {SD}")