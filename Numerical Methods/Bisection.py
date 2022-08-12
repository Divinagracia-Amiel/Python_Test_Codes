import math
Lb = float(input("lower bound: "))
Ub = float(input("upper bound: "))
times = int(input("how many iterations? "))
iteration = 1
MP = (Ub + Lb)/2

for i in range(1,times+1):
    print(f"Iteration {iteration}: ")
    print(f"Lower Bound: {Lb}")
    print(f"Upper Bound: {Ub}")
    PMP = MP
    Eq1_Lb = (Lb ** 3) - (3 * (Lb ** 2)) + Lb - 3
    Eq1_Ub = (Ub ** 3) - (3 * (Ub ** 2)) + Ub - 3
    Eq1_MP = (MP ** 3) - (3 * (MP ** 2)) + MP - 3
    
    if Eq1_MP * Eq1_Ub < 0:
        if MP < Ub:
            Lb = MP
            Ub = Ub
        else:
            Lb = Ub
            Ub = MP     
    elif Eq1_MP * Eq1_Lb < 0:
        if MP < Lb:
            Lb = MP
            Ub = Lb
        else:
            Lb = Lb
            Ub = MP
    PMP = (Ub + Lb)/2
    Ea = abs(((PMP - MP)/PMP)*100)
        
    print(f"midpoint is: {MP}" )
    print(f"f(x) Lb is: {Eq1_Lb}")
    print(f"f(x) Ub is: {Eq1_Ub}")
    print(f"f(x) MP is: {Eq1_MP}")
    print(f"Ea is: {Ea}%")
    print("")
    MP = PMP
    iteration += 1