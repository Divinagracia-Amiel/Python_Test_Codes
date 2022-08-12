import math
c1 = 3 * (math.log(xnmin, 10)) - (math.e ** -xnmin)
c2 = (2 * xnmin) * (math.cos(2 * xnmin)) - ((xnmin - 2) ** 2)
c3 = math.log(xnmin + 1, math.e) + math.cos(xnmin - 1)

d1 = (xnmin ** 3) + (4 * (xnmin ** 2)) - 10
d2 = math.sin(math.sqrt(xnmin)) - xnmin
d3 = ((xnmin - 2) ** 2) - math.log(xnmin, math.e)

e1 = (math.e ** ((xnmin ** 2) - 1)) + (10 * math.sin(2 * xnmin)) - 5
e2 = (xnmin ** 2) + math.atan(xnmin)
e3 = ((xnmin ** 3) * math.log(xnmin, math.e)) + (1 / math.cos(xnmin))