"""Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова 
должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой 
частоте появления — в лексикографическом порядке.
"""

dic = {}
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        for i in line:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

s = set()
for key, value in dic.items():
    s.add((value, key))

s = sorted(s, key=lambda x: x[1])
s = sorted(s, key=lambda x: x[0], reverse=True)

for i in s:
    print(i[1])
