low = True
data = -1
while low == True:
    try:
        low = int(input("Low end of range:\n"))
        high = int(input("High end of range:\n"))
    except ValueError:
        print("Please input an integer")
        low = True
        continue
    if low == 1:
        break
sum_in = 0
sum_out = 0
while data != 0:
    try:
        data = int(input("Enter data:\n"))
    except ValueError:
        print("Please input an integer")
        data = False
        continue
    if data == 0:
        break
    elif data < low or data > high:
        sum_out = sum_out + data
    else:
        sum_in = sum_in + data
print(f"Sum of in range values: {sum_in}\nSum of out of range values: {sum_out}")
    
        
    

    
