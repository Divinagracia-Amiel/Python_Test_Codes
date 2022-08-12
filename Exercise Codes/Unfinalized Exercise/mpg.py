init = -1
while init < 0:
    inMiles = int(input("Input initial mitles"))
    if inMiles < 0:
        break
    finMiles = int(input("Input final miles"))
    if inMiles > finMiles:
        print("Final should be larger than initial miles")
        inMiles = -1
        continue
    g = int(input("input gallons"))
    m = finMiles - inMiles
    mpg = m / g
    print(f"Miles per gallon: {mpg}")
    inMiles = -1
print("bye")
