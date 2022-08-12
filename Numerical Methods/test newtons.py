import math
xn = float(input("Xn: "))
times = int(input("how many iterations? "))
iteration = 1

for i in range(1,times):
    if iteration > 1:
        xn = xnplus
        prxnplus = xnplus  
    print(f"Iteration {iteration}: ")
    print(f"Xn: {xn}")
    
    fxn = round(xn - math.sin(xn) - (1/2), 8)
    fxnde = round(1 - math.cos(xn), 8)
    xnplus = round(xn - (fxn / fxnde), 8)
       
    if iteration > 1:
        Ea = round(abs(((xnplus - prxnplus)/xnplus)*100), 8)
        
    print(f"f(xn): {fxn}" )
    print(f"f'(x) xn is: {fxnde}")
    print(f"f(x) xnplus is: {xnplus}")
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")
    iteration += 1