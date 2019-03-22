"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее
время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
"""

import csv, math

list = []
with open("Crimes3.5.1.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3][9:11] == "15":
            a = row[5]
            list += [a]

dict = {}
for i in list:
     dict.update({i:list.count(i)})

m = max(dict.values())

for key,value in dict.items():
    if dict[key] == m:
        print(key)