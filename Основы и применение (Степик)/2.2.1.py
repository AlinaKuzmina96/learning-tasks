"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
"""

import datetime

s = input().split()
year, month, day = int(s[0]), int(s[1]), int(s[2])
n = int(input())
a = datetime.date(year, month, day)
b = datetime.timedelta(n)
s = a + b
print(s.year, s.month, s.day)
