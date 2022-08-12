import math
x = int(input("Enter x: "))
sum_t = 1 + x
n = 1
cnt_fct = 2
fact = 2
lw_fact = fact
power = 2
term = 0.1
print(f"n: {n} term: {x}     sum: {sum_t}")
while term > 1E-12:
    if term == 0.1:
        term = 0
    for i in range(1, fact+1):
        if lw_fact > 1:
            fact *= (lw_fact-1)
        lw_fact -= 1
    num = x ** power
    term = num / fact
    cnt_fct +=  1
    fact = cnt_fct
    lw_fact = fact
    power += 1
    sum_t +=  term
    n += 1
    print(f"n: {n}  term: {term}        sum: {sum_t}")
real = math.exp(x)
print(f"real e^x: {real}")
    
    
    