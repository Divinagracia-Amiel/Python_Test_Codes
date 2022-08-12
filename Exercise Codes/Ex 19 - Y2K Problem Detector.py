YoB = -1
Cur_Y = -1
while YoB > 99 or YoB < 0 or Cur_Y > 99 or Cur_Y < 0:
    try:
        YoB = int(input("When are you born?\n*note: 1994 is 94, 1956 is 56\n"))
        Cur_Y = int(input("What is the current year?\n*note: 1994 is 94, 1956 is 56\n"))
    except ValueError:
        print("please enter a number")
        continue
    if YoB > 99 or YoB < 0 or Cur_Y > 99 or Cur_Y < 0:
        print("Enter a postive 2-digit number\n")
        cont = input("Press ENTER to continue...")
        continue
print(f"Year of birth:\n{YoB}\n",
      f"Current year:\n{Cur_Y}\n")
if Cur_Y < YoB:
    Age = (Cur_Y + 100) - YoB
else:
    Age = Cur_Y - YoB
print(f"Your age: {Age}")
        
    
