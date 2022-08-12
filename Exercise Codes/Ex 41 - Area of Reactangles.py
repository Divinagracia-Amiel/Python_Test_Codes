import math
x_1 = -1
while x_1 < 0 or y_1 < 0 or x_2 < 0 or y_2 < 0:
    try:
        x_1 = int(input("First corner X coordinate:\n"))
        if x_1 < 0:
            print("Please enter a positive number")
            continue
        y_1 = int(input("First corner Y coordinate:\n"))
        if y_1 < 0:
            print("Please enter a positive number")
            continue
        x_2 = int(input("Second corner X coordinate:\n"))
        if x_2 < 0:
            print("Please enter a positive number")
            continue
        y_2 = int(input("Second corner Y coordinate:\n"))
        if y_2 < 0:
            print("Please enter a positive number")
            continue
    except ValueError:
        print("Please enter an integer")
    height = math.sqrt((y_2 - y_1) ** 2)
    width = math.sqrt((x_2 - x_1) ** 2)
    area = height * width
    if area == 0:
        break
    print(f"Width: {width}\nHeight: {height}\nArea: {area}")
    x_1 = -1
    continue
