"""Для данного числа n<100 закончите фразу “На лугу пасется...” одним из 
возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя 
слово “корова”."""

n = str(input())
l = len(n) - 1
if len(n) >= 2:
    if int(n[l]) == 1 and int(n[l-1:l+1]) != 11:
        print(n, 'korova')
    elif 1 < int(n[l]) < 5 and 15 < int(n[l-1:l+1]):
        print(n, 'korovy')
    else:
        print(n, 'korov')
else:
    if int(n) == 1:
        print(n, 'korova')
    elif 1 < int(n) < 5:
        print(n, 'korovy')
    else:
        print(n, 'korov')
