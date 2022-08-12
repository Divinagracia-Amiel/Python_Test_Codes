init = -1
while init < 0:
    try:
        init = int(input("Initial Miles:\n"))
        if init < 0:
            break
        final = int(input("Final Miles:\n"))
        if final < init:
            print("Final miles should be larger than initial miles")
            init = -1
            continue
        gallons = int(input("Gallons:\n"))
    except ValueError:
        print("Please enter an integer")
        init = -1
        continue
    dis = final - init
    mpg = dis / gallons
    print(f"Miles per Gallon: {mpg}\n")
    init = -1
print("bye")
    
    
    
    