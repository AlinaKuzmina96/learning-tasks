"""Даны произвольные действительные коэффициенты a, b, c. Решите уравнение ax²+bx+c=0."""

import math

a, b, c = float(input()), float(input()), float(input())

if a == 0 and b == 0 and c == 0:
    print(3)
elif (a == 0 and b == 0 and c != 0) or (a == 0 and c == 0 and b != 0):
    print(0)
elif (b == 0 and c == 0 and a != 0):
    print(0)
elif (a == 0 and c == 0 and b != 0) or (b == 0 and c == 0 and a != 0):
    print(1, 0)
elif a == 0 and b != 0 and c != 0:
    print(1, -c / b)
elif b == 0 and a != 0 and c != 0:
    if (-c / a) >= 0:
        print(2, -math.sqrt(-c / a), math.sqrt(-c / a))
    else:
        print(0)
elif c == 0 and a != 0 and b != 0:
    if (-b / a) > 0:
        print(2, 0, -b/a)
    else:
        print(2, -b/a, 0)
else:
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        x = sorted([x2, x1])
        print(2, x[0], x[1])
    elif D == 0:
        print(1, (-b) / (2 * a))
    else:
        print(0)
