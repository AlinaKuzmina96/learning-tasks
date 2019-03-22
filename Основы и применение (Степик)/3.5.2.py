"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name,
которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.
"""

import json

js = json.loads(input())
#js =[{"name": "But", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]
#js1 =[{"name": "Ar", "parents": []}, {"name": "B", "parents": ["Ar", "C"]}, {"name": "C", "parents": ["Ar"]}]
#js2 = [{"name": "A", "parents": ["But", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "But", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]

dict = {}

for i in js:
    for j in i["parents"]:
        dict.update({j:[]})

for i in js:
    if i["name"] in dict:
        dict[i["name"]] += [i["name"]]
    else:
        dict.update({i["name"]:[i["name"]]})

for i in js:
    for k in i["parents"]:
        if k in dict:
            dict[k] += [i["name"]]
        else:
            dict.update({k: [i["name"]]})

def rec(a):
    for j in js:
        if a in j["parents"]:
            for k in i["parents"]:
                dict[k] += [j["name"]]
            rec(j["name"])

for i in js:
    rec(i["name"])

for key,value in dict.items():
    s = []
    for i in value:
        if i not in s:
            s += [i]
    dict[key] = len(s)

for k in sorted(dict.keys()):
    print (k, ':', dict[k])