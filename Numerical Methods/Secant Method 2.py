import math
xnmin = float(input("Xn-1: "))
xn = float(input("Xn: "))
times = int(input("how many iterations? "))
iteration = 1
print(f"Iteration {iteration}: ")
print(f"Xn-1: {xnmin}")
print(f"Xn: {xn}")
fxnmin = round((2 * xnmin) * (math.cos(2 * xnmin)) - ((xnmin - 2) ** 2), 8)
fxn = round((2 * xn) * (math.cos(2 * xn)) - ((xn - 2) ** 2), 8)
xnplus = round(xn - ((fxn*(xn - xnmin))/(fxn - fxnmin)), 8)
fxnplus = round((2 * xnplus) * (math.cos(2 * xnplus)) - ((xnplus - 2) ** 2), 8)
print(f"xnplus is: {xnplus}" )
print(f"f(x) xnmin is: {fxnmin}")
print(f"f(x) xn is: {fxn}")
print(f"f(x) xnplus is: {fxnplus}")
print("")
iteration = 2

for i in range(1,times):
    if iteration > 1:
        prxnplus = xnplus
    xnmin = xn
    xn = xnplus
    fxnmin = fxn
    fxn = fxnplus
    print(f"Iteration {iteration}: ")
    print(f"Xn-1: {xnmin}")
    print(f"Xn: {xn}")
    
    xnplus = round(xn - ((fxn*(xn - xnmin))/(fxn - fxnmin)), 8)
    fxnplus = round((2 * xnplus) * (math.cos(2 * xnplus)) - ((xnplus - 2) ** 2), 8)
       
    if iteration > 1:
        Ea = round(abs(((xnplus - prxnplus)/xnplus)*100), 8)
        
    print(f"xnplus is: {xnplus}" )
    print(f"f(x) xnmin is: {fxnmin}")
    print(f"f(x) xn is: {fxn}")
    print(f"f(x) xnplus is: {fxnplus}")
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")
    iteration += 1