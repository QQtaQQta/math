#14

import math

x = float(input('enter x: '))

z1 = (math.cos(math.radians(x)) + math.sin(math.radians(x))) / (math.cos(math.radians(x)) - math.sin(math.radians(x)))

z2 = math.tan(math.radians(x))**2 - 1 / math.cos(math.radians(x))**2

print("z1 = ", z1)
print("z2 = ", z2)