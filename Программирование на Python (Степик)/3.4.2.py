"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово
в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое
(можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.
"""

import math

text = ""
with open("text3.4.2.txt", "r") as doc:
    for line in doc:
        text += line.strip()
        text += " "
dict = {}
text = text.lower().split()
for i in text:
    dict.update({i: text.count(i)})
a = max(dict.values())
list = []
for key, value in dict.items():
    if value == a:
        list.append(key)
list = sorted(list)
print(list[0], dict[list[0]])
