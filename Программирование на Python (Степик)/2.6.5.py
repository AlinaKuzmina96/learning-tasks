"""
Выведите таблицу размером n, заполненную числами от $1$ до $n^2$ по спирали, выходящей из левого верхнего
угла и закрученной по часовой стрелке
"""

n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
s = 1
k = 0
l = n-1
while s <= n * n:
    for i in range(k, k+1):
        for j in range(k, l+1):
            a[i][j] = s
            s += 1
    for j in range(l, l+1):
        for i in range(k+1, l+1):
            a[i][j] = s
            s += 1
    for j in range(l-1, k-1, -1):
        for i in range(l, l+1):
            a[i][j] = s
            s += 1
    for j in range(k, k+1):
        for i in range(l-1, k, -1):
            a[i][j] = s
            s += 1
    k += 1
    l -= 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
