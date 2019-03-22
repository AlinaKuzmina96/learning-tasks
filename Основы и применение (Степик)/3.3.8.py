"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
"""

import sys, re

pattern = r"\b(\w)(\w)"
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r"\2\1", line)
    print(line)