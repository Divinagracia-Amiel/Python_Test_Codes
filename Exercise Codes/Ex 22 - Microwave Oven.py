Items = -1
Time_H = -1
while Items < 0 or Time_H < 0:
    try:
        Items = int(input("How many items do you intend to microwave? "))
        Time_H = int(input("How many minutes does one of the items is needed to be microwaved "))
    except ValueError:
        print("Please input an integer.")
        continue
    if Items < 0 or Time_H < 0:
        print("Please input a positive integer")
        continue
if Time_H == 0:
    print("The heating time is 0")
elif Items == 1:
    Time = Time_H
    print(f"The recommended heating time is {Time} minutes.")
elif Items == 2:
    Time = Time_H * 1.5
    print(f"The recommended heating time is {Time} minutes.")
elif Items == 3:
    Time = Time_H * 2
    print(f"The recommended heating time is {Time} minutes.")
elif Items > 3:
    print(f"Heating more than 3 items is dangerous thus not recommended")

        
    
    
        

