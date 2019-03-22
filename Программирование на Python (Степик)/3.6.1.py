"""
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
"""

import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/833.txt')
t = r.text
t = t.splitlines()
l = len(t)
print(l)