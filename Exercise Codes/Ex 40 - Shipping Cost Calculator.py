weight = 1
handling = 3
sh_in = 3
sh_cost = 0
sh_extra = 0
while weight > 0:
    try:
        weight = float(input("Weight of order:\n"))
    except ValueError:
        print("Please print an integer")
        continue
    ov_load = weight / 10
    if ov_load > 1:
        xtra = (weight % (2 ** 100))-10
        sh_extra = xtra * .25
        sh_cost = sh_in + sh_extra
    else:
        sh_cost = 3
    print(f"Shipping Cost: ${sh_cost}\n")
print("bye")