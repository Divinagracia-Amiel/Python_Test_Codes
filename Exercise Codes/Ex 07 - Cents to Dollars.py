cents = False
while cents == False:
    try:
        cents = int(input("Input the cents:\n"))
    except ValueError:
        print("Please enter an integer.")
        continue
    break
dollars = int(cents / 100)
rem = cents % 100
print(f"That is {dollars} dollars and {rem} cents")
    