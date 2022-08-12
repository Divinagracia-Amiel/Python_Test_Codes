a = 2
b = 1
while b < a:
    try:
        a = int(input("Enter starting value:\n"))
        b = int(input("Enter end value:\n"))
    except ValueError:
        print("Please enter an integer")
        continue
    if a > b:
        print("please input a number in a way that the second number is larger than the first one")
        continue
print("")
for i in range(a,b+1):
    print(i)
    
