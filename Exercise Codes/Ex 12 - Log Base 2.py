import math
x = float(input("Input a number to find its base 2 logarithm"))
log_b2 = math.log(x) / math.log (2)
print(f"The base 2 logarithm of {x} is equal to %.3f" %(log_b2))