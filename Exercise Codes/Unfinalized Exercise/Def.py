h = 0
w = 0
name = ''
def bmi(name, h, w):
    bmi = w / (h ** 2)
    print(f"bmi: {bmi}")
    if bmi < 25:
        return f"{name}, not overweight"
    else:
        return f"{name}, overweight"
def check():
    count = 0
    sp_ = ''
    while name != sp_:
        x = 0
        limit = 1
        while x < limit:
            sp_ += ' '
            x += 1
            count += 1
        if count > 100:
            break        
    return sp_
    
print("Enter nothing to name to exit")
loop = True
while loop == True:
    try:
        name = input("What is your name? ")
        if name == check():
            break
        h = float(input("What is your height?(in meters) " ))
        if h < 0:
            print("Please enter a positive value")
            continue
        if h == 0:
            print("Undefined so please try again")
            continue
        w = float(input("What is your weight?(in kg) "))
        if w < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a number in weight or height")
        continue
    bmi = bmi(name, h, w)
    print(bmi + '\n')
print("See you again!")