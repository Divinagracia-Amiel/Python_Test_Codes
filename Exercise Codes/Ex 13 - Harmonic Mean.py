print("Harmonic Mean Calculator")
x = float(input("Enter a first number: "))
y = float(input("Enter a second number: "))
Mean = (x + y) / 2
HarMean = 2 / ((1 / x) + (1 / y))
print("Arithmetic Mean: %.2f\nHarmonic Mean: %.2f" %(Mean, HarMean))
