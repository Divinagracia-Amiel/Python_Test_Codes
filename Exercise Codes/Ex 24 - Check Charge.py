print("Charge Check")
sa = -1
ca = -1
while ca < 0 or sa < 0:
    try:
        sa = float(input("What is the balance in your savings account?(in dollars): "))
        ca = float(input("What is the balance in your checking account?(in dollars): "))
    except ValueError:
        print("Please write a number.")
        continue
    if ca < 0 or sa < 0:
        print("Please write a poistive number.")
        continue
if ca > 1000 or sa > 1500:
    print("No charge per check.")
else:
    print("0.15$ charge per check.")
