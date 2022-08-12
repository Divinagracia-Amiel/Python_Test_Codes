limit = False
while limit == False:
    try:
        limit = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a number")
        continue
_sumsq = 0
_sumcb = 0
count = 1
for i in range(1, limit+1):
    sq = count ** 2
    cb = count ** 3
    _sumsq = _sumsq + sq
    _sumcb = _sumcb + cb
    count = count + 1
print(f"The sum of squares is: {_sumsq}\nThe sum of cubes is: {_sumcb}")
