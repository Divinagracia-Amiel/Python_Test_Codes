times = int(input("How many iterations? "))
x1 = float(input("initial 1 "))
x2 = float(input("initial 2 "))
x3 = float(input("initial 3 "))
iteration = 1

for i in range(1,times+1):
    print(f"Iteration {iteration}: ")
    f1 = round(((2 * x3) - x2 + 8)/7,5)
    f2 = round((7 - x1 + x3)/-5,5)
    f3 = round((1 - (2 * x1) - (3 * x2))/6,5)
    x1 = f1   
    x2 = f2  
    x3 = f3  
    print(f"x1 = {x1} ")
    print(f"x2 = {x2} ")
    print(f"x3 = {x3} ")
    iteration += 1
    