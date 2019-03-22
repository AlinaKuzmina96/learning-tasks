"""Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое 
наибольшее число подряд идущих элементов этой последовательности равны друг другу."""

s = []
t = []
p = 1
while True:
    n = int(input())
    if n != 0:
        t.append(n)
        if len(t) != 1 and n == t[len(t)-2]:
            p += 1
        else:
            s.append([t[len(t)-2], p])
            p = 1
    else:
        s.append([t[len(t)-1], p])
        break

m = s[0][1]
for i in range(1, len(s)):
    if s[i][1] > m:
        m = s[i][1]

print(m)
