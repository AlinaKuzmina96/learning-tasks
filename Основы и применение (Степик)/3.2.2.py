"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
"""

s, t = str(input()), str(input())

def count(s, t, i=0):
    if t in s:
        index = s.find(t)
        s = s[index+1:]
        i += 1
        return count(s, t, i)
    else:
        return i

print(count(s, t))