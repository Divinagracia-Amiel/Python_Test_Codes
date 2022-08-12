import math
xindeg = 30
xinrad = xindeg * (math.pi / 180)
sine = math.sin(xinrad)
cosine = math.cos(xinrad)
sqr = (sine ** 2) + (cosine ** 2)
print(f"sine: {sine}\tcosine: {cosine}\tsum: {sqr}")