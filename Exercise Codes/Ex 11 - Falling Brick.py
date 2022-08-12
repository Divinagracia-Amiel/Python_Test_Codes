g = 32.174
c = 1/2
print("Imagine a brick falling down a tower")
sec = float(input("How many seconds did the brick fall until impact from the ground?"))
d = (c * g * (sec ** 2))
print("The distance travelled was:", (format(d, ',.3f')), "feet")

