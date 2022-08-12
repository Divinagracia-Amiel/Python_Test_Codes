import math
xn = float(input("Xn: "))
times = int(input("how many iterations? "))
iteration = 1


for i in range(1,times+1):      
    print(f"Iteration {iteration}: ")
    print(f"Xn: {xn}")
    if iteration > 1:
        pxn = xn
    gxn = math.sqrt(10 / (4 + xn))
    gxn_rn = round(gxn, 8)
    xn = gxn
  
    if iteration > 1:
        Ea = round(abs(((xn - pxn)/xn)*100), 8)
        
    print(f"g (xn) is: {gxn_rn}" )
    if iteration > 1:
        print(f"Ea is: {Ea}%")
    print("")       
    iteration += 1