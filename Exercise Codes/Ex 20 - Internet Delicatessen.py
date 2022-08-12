print("Welcome to Sam and Ella's Delicatessen")
order = input("What are you going to order?")
price = False
while price == False:
    try:
        price = float(input("How much is the item you ordered?(in cents)"))
    except ValueError:
        print("Enter a price number")
        continue
    if price < 0:
        print("Enter a positive number")
        continue
Ovdev = -1
while Ovdev < 0 or Ovdev > 1:
    try:
        Ovdev = int(input("Is it overnight delivery?\n"
                          "Press 1 for yes\nPress 0 for no\n"))
    except ValueError:
        print("Please enter a number")
        continue
    if Ovdev < 0 or Ovdev > 1:
        print("Enter 1 or 2 only")
        continue
pr_D = price / 100
Ovdev_pr = 0
if Ovdev == 1:
    Ovdev_pr = 5
if pr_D < 10 and pr_D > 0:
    sh_pr =  2
elif pr_D > 10:
    sh_pr =  3
sh_total = Ovdev_pr + sh_pr
total = pr_D + sh_total
print(f"Invoice:\n{order}: ${pr_D}\nshipping: ${sh_total}\ntotal: ${total}")

