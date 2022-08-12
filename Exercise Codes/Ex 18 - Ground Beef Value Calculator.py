print("Ground Beef Value Calculator")
Prlbs_A = -1
Prlbs_B = -1
Perlean_A = -1
Perlean_B = -1 
while Prlbs_A < 0 or Prlbs_B < 0:
    try:
        Prlbs_A = float(input("What is the price per pound of package A? "))
        Prlbs_B = float(input("What is the price per pound of package B? "))
    except ValueError:
        print("Please enter a number")
        continue
    if Prlbs_A < 0 or Prlbs_B < 0:
        print("Please enter a positive number")
        continue
while Perlean_A < 0 or Perlean_A > 100 or Perlean_B < 0 or Perlean_B > 100:
    try:
        Perlean_A = int(input("What is the percent lean in package A? "))
        Perlean_B = int(input("What is the percent lean in package B? "))
    except ValueError:
        print("Please enter an integer")
        continue
    if Perlean_A < 0 or Perlean_A > 100 or Perlean_B < 0 or Perlean_B > 100:
        print("Please enter an integer between 0 to 100")
        continue
LeanPer_A = Perlean_A / 100
LeanPer_B = Perlean_B / 100
Cost_A = Prlbs_A / LeanPer_A
Cost_B = Prlbs_B / LeanPer_B
print(f"Price per pound package A:\n{Prlbs_A}\n",
      f"Percent lean package A:\n{Perlean_A}\n",
      f"Price per pound package B:\n{Prlbs_B}\n",
      f"Percent lean package B:\n{Perlean_B}\n")
print(f"Package A cost per pound of lean: %.3f\n" %(Cost_A),
      f"Package B cost per pound of lean: %.3f\n" %(Cost_B))
if Cost_A < Cost_B:
    print("Package A is the best value")
elif Cost_B < Cost_A:
    print("Package B is the best value")
else:
    print("They are equal in value")
    
    
    
    
    
    
    
    
    
    
    
