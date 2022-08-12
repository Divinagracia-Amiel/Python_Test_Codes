n = -1
while n < 0:
    try:
        base = float(input("Enter X\n"))
        n = int(input("Enter N\n"))
    except ValueError:
        print("Please enter a number")
        continue
    if n < 0:
        print("N must be a positive number")
        continue
power = base ** n
print(f"{base} raised to the power of {n}: %.5f" %(power))