"""
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и
производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
"""

with open('nabor3.4.1.txt', 'r') as inf:
    s = inf.readline().strip()

with open('answer3.4.1.txt', 'w') as ouf:
    s1 = ""
    for i in range(len(s)):
        if "a" <= s[i].lower() <= "z":
            a = s[i]
            i += 1
            count = ""
            while '0' <= s[i] <= '9':
                count += s[i]
                if i + 1 <= len(s):
                    i += 1
            r = a*int(count)
            s1 += r
    ouf.write(s1)
