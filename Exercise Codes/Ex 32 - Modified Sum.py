limit = False
while limit == False:
    try:
        limit = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a number")
        continue
_sum = 0
n = 0
if limit >= 0:
    for i in range(1, limit+1):
        _sum = _sum + (1 /(i))
elif limit < 0:
    limit = -limit
    for i in range(1, limit+1):
        _sum = _sum + (1 /(i))
print(f"Sum is: {_sum}")
