import math
xnmin = float(input("Xn-1: "))
xn = float(input("Xn: "))
times = int(input("how many iterations? "))
iteration = 1


for i in range(1,times+1):      
    print(f"Iteration {iteration}: ")
    print(f"Xn-1: {xnmin}")
    print(f"Xn: {xn}")
    if iteration > 1:
        prxnplus = xnplus
    fxnmin = round((math.tan(xnmin) - xnmin - 1), 8)
    fxn = round((math.tan(xn) - xn - 1), 8)
    xnplus = round(xn - ((fxn*(xn - xnmin))/(fxn - fxnmin)), 8)
    fxnplus = round((math.tan(xnplus) - xnplus - 1), 8)
    
    if fxnplus * fxn < 0:
        if xnplus < xn:
            xnmin = xnplus
            xn = xn
        else:
            xnmin = xn
            xn = xnplus     
    elif fxnplus * fxnmin < 0:
        if xnplus < xnmin:
            xnmin = xnplus
            xn = xnmin
        else:
            xnmin = xnmin
            xn = xnplus
    if iteration > 1:
        Ea = round(abs(((xnplus - prxnplus)/xnplus)*100), 4)
        
    print(f"xnplus is: {xnplus}" )
    print(f"f(x) xnmin is: {fxnmin}")
    print(f"f(x) xn is: {fxn}")
    print(f"f(x) xnplus is: {fxnplus}")
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")
    
    iteration += 1