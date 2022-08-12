cyc = False
while cyc == False:
    try:
        cyc = int(input("How many numbers will be added up? "))
    except ValueError:
        print("Please input an integer")
        continue
    if cyc < 0:
        print("Please input a positive number")
        cyc = False
        continue
count = 1
_sum = 0
while count <= cyc:   
    try:
        add = int(input("Enter an integer "))
    except ValueError:
        print("Enter an integer")
        continue
    _sum = _sum + add
    count = count + 1
print(f"The sum is {_sum}")
    

