rate = float(input("Input cost per kilowatt-hour in cents "))
usage = False
while usage == False:
    try:
        usage = int(input("How many hours did you use the appliance this year "))
    except ValueError:
        print("Please enter an integer")
        continue
    break
Costin_C = rate * usage
Costin_D = Costin_C / 100
print("The Annual Cost is: $%.3f" %(Costin_D))