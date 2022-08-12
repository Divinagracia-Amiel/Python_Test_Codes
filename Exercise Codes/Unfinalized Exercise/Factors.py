def add(x):
    total = 0
    for i in x:
        total += i
    return total 
def check(x):
    fact_list = []
    limit = int(x/2)
    for i in range(1, limit+1):
        fact = x % i
        if fact == 0:
            fact_list.append(i)
    return fact_list
    print
init = int(input("Input a number: "))
fact = check(init)
_sum = add(fact)
half = init/2
key = 0
print(f"factors: ", end='')
print(*fact, sep=', ')
print(f"Sum of its factors: ", end='')
print(*fact, sep='+', end=' = ')
print(_sum)
print(f"Half of number: {init}/2 = {half}")
if _sum > half:
    print(f"{init} is DWARF")
else:
    print(f"{init} is NOT DWARF")






