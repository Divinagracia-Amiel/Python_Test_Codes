times = int(input("How many iterations? "))
x1 = float(input("initial 1 "))
x2 = float(input("initial 2 "))
iteration = 1

for i in range(1,times+1):
    print(f"Iteration {iteration}: ")
    f1 = round((6 + x2)/7,5)
    x1 = f1
    print(f"x1 = {x1} ")
    f2 = round((4 + x1)/5,5)
    x2 = f2
    print(f"x2 = {x2} ")
    iteration += 1
    