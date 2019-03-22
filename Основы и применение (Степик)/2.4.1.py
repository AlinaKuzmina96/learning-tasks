"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
"""

with open("text2.4.1.txt", "r") as f, open("text12.4.1.txt", "w") as g:
    lst = []
    for line in f:
        lst.append(line.strip())
    lst = reversed(lst)
    for i in lst:
        g.write(i+'\n')