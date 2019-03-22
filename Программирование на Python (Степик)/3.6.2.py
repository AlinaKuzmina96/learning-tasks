"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
t = r.text
t = t.split()
while t[0] != 'We':
	u = str(t[0])
	r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+u)
	t = r.text
	t = t.split()
with open('text.txt', 'w') as ouf:
	ouf.write(r.text)	
