"""Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" 
в одном из трех смыслов:
    кошки (животные)
    UNIX-утилита cat для вывода содержимого файлов
    версии операционной системы OS X, названные в честь семейства кошачьих
Ваша задача — найти два предложения, которые ближе всего по смыслу к расположенному в 
самой первой строке. В качестве меры близости по смыслу мы будем использовать косинусное 
расстояние."""

import re
from scipy.spatial import distance

word = ''
lines = []
with open('alignment_of_sentences.txt') as f:
	for line in f:
		word += line.strip().lower()
		lines += [line.strip().lower()]
		
words =  re.split('[^a-z]', word)
while '' in words:
	words.remove('')

words = list(set(words))
dic = {}
for i in range(len(words)):
	dic[i]= words[i]

matrix = [[0 for i in range(len(words))] for i in range(len(lines))]

for i in range(len(lines)):
	ls =  re.split('[^a-z]', lines[i])
	for j in range(len(words)):
		matrix[i][j] = ls.count(words[j])

m = []
for i in range(1,len(matrix)):
	m.append(distance.cosine(matrix[0], matrix[i]))

print(m.index(sorted(m)[0])+1, m.index(sorted(m)[1])+1)
