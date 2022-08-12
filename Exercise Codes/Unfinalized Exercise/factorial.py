fact = int(input(""))
lw_fact = fact
for i in range(1, fact+1):
    if lw_fact > 1:
        fact = fact * (lw_fact-1)
    lw_fact = lw_fact - 1
print(fact)