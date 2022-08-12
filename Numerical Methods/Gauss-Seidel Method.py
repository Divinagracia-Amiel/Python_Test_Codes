times = int(input("How many iterations? "))
x1 = float(input("initial 1 "))
x2 = float(input("initial 2 "))
x3 = float(input("initial 3 "))
iteration = 1

for i in range(1,times+1):
    print(f"Iteration {iteration}: ")
    f1 = round((5 + (2 * x2) + (3 * x3))/6,5)
    x1 = f1
    print(f"x1 = {x1} ")
    f2 = round((-1 - x1 + x3)/5,5)
    x2 = f2
    print(f"x2 = {x2} ")
    f3 = round((3 - (4 * x1) - (5 * x2))/12,5)
    x3 = f3
    print(f"x3 = {x3} ")
    iteration += 1
    
    
       