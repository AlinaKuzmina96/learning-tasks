"""
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки
одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
"""

str, str1, str2, str3 = input(), input(), input(), input()
dict, dict1 = {}, {}
str21, str31 = "", ""

for i in range(len(str)):
    dict[str[i]] = str1[i]
    dict1[str1[i]] = str[i]

for i in str2:
    str21 += dict[i]
for i in str3:
    str31 += dict1[i]

print(str21)
print(str31)
