"""
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.
"""

import sys, re

pattern = r"[01]+"
for line in sys.stdin:
    line = line.rstrip()
    a = re.findall(pattern, line)
    if len(a) == 1:
        t = int(a[0], 2)
        if t % 3 == 0:
            print(line)