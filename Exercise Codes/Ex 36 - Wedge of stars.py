quan = -1
while quan < 0:
    try:
        quan = int(input("Enter initial number of stars:\n"))
    except ValueError:
        print("Please enter an integer")
        continue
    if quan < 0:
        print("Please enter a positive integer")
        continue
count = 0
for i in range(1, quan+1):
    while count < quan:
        print("*", end="")
        count = count + 1
    print("")
    count = 0
    quan = quan - 1