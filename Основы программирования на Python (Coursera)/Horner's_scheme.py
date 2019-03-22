"""Дан многочлен P(x) = a[n] xⁿ+a[n-1] xⁿ⁻¹+...+a[1] x+a[0] и число x. Вычислите значение 
этого многочлена, воспользовавшись схемой Горнера:

P(x) = ( ... ( ( ( a[n] x + a[n-1] ) x + a[n-2] ) x + a[n-3] ) ... ) x + a[0]"""

n = int(input())
x = float(input())
a = []
for i in range(n+1):
    a. append(float(input()))
if n == 0:
    print(a[0])
else:
    s = a[0] * x
    for i in range(1, len(a) - 1):
        s = (s + a[i]) * x
    s += a[len(a)-1]
    print(s)
