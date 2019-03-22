"""Даны числа a, b, c, d, e, f. Решите систему линейных уравнений
ax + by = e
cx + dy = f"""

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

if c != 0:
    y = (e - a * f / c) / (b - a * d / c)
    x = (f - d * y) / c
else:
    if d != 0 and a != 0:
        y = f / d
        x = (e - b * y) / a
if str(x)[-2:] == '.0':
    x = int(x)
elif str(y)[-2:] == '.0':
    y = int(y)
print(x, y)
