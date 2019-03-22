"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
"""

import sys, re

pattern = r"(\w)(\1+)"
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r"\1", line)
    print(line)