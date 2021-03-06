"""Первая строка входных данных содержит число n — наибольшее число, которое мог загадать Август. 
Далее идут строки, содержащие вопросы Беатрисы. Каждая строка представляет собой набор чисел, 
разделенных пробелами. После каждой строки с вопросом идет ответ Августа: YES или NO. Наконец, 
последняя строка входных данных содержит одно слово HELP.
Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.
"""

n = int(input())
lst = set(range(1, n+1))

while True:
    s = input()
    if s != 'HELP':
        if s == 'YES':
            lst &= set(lst1)
        elif s == 'NO':
            lst -= lst1
        else:
            lst1 = set(int(i) for i in s.split())
    else:
        print(*(sorted(lst)))
        break
