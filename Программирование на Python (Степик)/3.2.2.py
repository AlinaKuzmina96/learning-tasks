"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести
получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число
его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.
"""

str = input().split()
dict = {}
for i in str:
    if i.lower() in dict:
        dict[i.lower()] += 1
    else:
        dict.update({i.lower(): 1})

for key, value in dict.items():
    print(key, value)