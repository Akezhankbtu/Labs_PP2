import math
n = int(input("количество сторон: "))
s = float(input("длину стороны: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"Площадь: {area:.0f}")
