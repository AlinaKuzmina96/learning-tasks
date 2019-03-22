lst = []
for i in range(4):
    n = input()
    n = ''.join(n.split('-'))
    if len(n) == 7:
        n = '495' + n
    n = ''.join(n.split('('))
    n = ''.join(n.split(')'))
    lst.append(n[-10:])

for i in range(1, 4):
    if lst[i] == lst[0]:
        print('YES')
    else:
        print('NO')
