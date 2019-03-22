"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
"""

import sys, re

pattern = r"a+\b"
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, "argh", line, 1, re.IGNORECASE)
    print(line)