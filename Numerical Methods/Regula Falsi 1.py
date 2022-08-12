import math
xnmin = float(input("Xn-1: "))
xn = float(input("Xn: "))
times = int(input("how many iterations? "))
iteration = 1


for i in range(1,times+1):      
    print(f"Iteration {iteration}: ")
    print(f"Xn: {xn}")
    if iteration > 1:
        prxnplus = xnplus
    fxnmin = round(math.sin(2*xnmin) - (math.e ** (xnmin - 1)), 8)
    fxn = round(math.sin(2*xn) - (math.e ** (xn - 1)), 8)
    xnplus = round(xn - ((fxn*(xn - xnmin))/(fxn - fxnmin)), 8)
    fxnplus = round(math.sin(2*xnplus) - (math.e ** (xnplus - 1)), 8)
        
    print(f"g(xn): {xnplus}" )
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")
    
    iteration += 1