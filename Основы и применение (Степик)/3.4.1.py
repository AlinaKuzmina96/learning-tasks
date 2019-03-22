"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
из C в B можно перейти за один переход.
Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
"""

import requests, re

#a = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
#b = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
a, b = input(), input()
flag = "No"

res = requests.get(a)
pattern = r"<a href=[\"|\'](.*)[\"|\']"
list = re.findall(pattern, res.text)
for i in list:
    res1 = requests.get(i)
    list1 = re.findall(pattern, res1.text)
    if b in list1:
        flag = "Yes"

print(flag)
