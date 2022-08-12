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
    fxnmin = round((math.e ** (-2 * xnmin)) + (4 * (xnmin ** 2)) - 36, 5)   
    fxn = round((math.e ** (-2 * xn)) + (4 * (xn ** 2)) - 36, 5)
    xnplus = round(xn - ((fxn*(xn - xnmin))/(fxn - fxnmin)), 5)
    fxnplus = round((math.e ** (-2 * xnplus)) + (4 * (xnplus ** 2)) - 36, 5)
    
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
        Ea = round(abs(((xnplus - prxnplus)/xnplus)*100), 5)
        
    print(f"xnplus is: {xnplus}" )
    print(f"f(x) xnmin is: {fxnmin}")
    print(f"f(x) xn is: {fxn}")
    print(f"f(x) xnplus is: {fxnplus}")
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")
    
    iteration += 1