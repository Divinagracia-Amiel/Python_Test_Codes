print("Welcome to Yertle's Quest")
name = input("Enter the name of your character: ")
sk_pts = 15
print(f"You have {sk_pts} pts left")
strength = -1
HP = -1
luck = -1
while strength < 0 or strength > 15:
    try:
        strength = int(input("Enter your character's strength(1-10):\n"))     
    except ValueError:
        print("\nPlease enter an integer from 1-10")
        input("press ENTER to continue...")
        continue
    if strength < 0 or strength > 15:
        print("\nPlease enter a positive integer from 1-10")
        input("press ENTER to continue...")
        continue
while HP < 0 or HP > 15:
    sk_pts = sk_pts - strength
    print(f"You have {sk_pts} pts left")
    try:
        HP = int(input("Enter your character's health(1-10):\n"))
    except ValueError:
        print("\nPlease enter an integer from 1-10")
        input("press ENTER to continue...")
        continue
    if HP < 0 or HP > 15:
        print("\nPlease enter a positive integer from 1-10")
        input("press ENTER to continue...")
        continue
while luck < 0 or luck > 15:
    sk_pts = sk_pts - HP
    print(f"You have {sk_pts} pts left")
    try:
        luck = int(input("Enter your character's luck(1-10):\n"))
    except ValueError:
        print("\nPlease enter an integer from 1-10")
        input("press ENTER to continue...")
        continue
    if luck < 0 or luck > 15:
        print("\nPlease enter a positive integer from 1-10")
        input("press ENTER to continue...")
        continue
Total = strength + HP + luck
if Total > 15:
    print(f"You gave your character to many points!\nDefault values has been assigned:\n{name}, strength: 5, health: 5, luck: 5.")
else:
    print(f"Once again, welcome to Yertle's Quest, {name}.\nHere is your character's stats:\nstrength: {strength}\nhealth: {HP}\nluck: {luck}")
        
        
        
        
        
