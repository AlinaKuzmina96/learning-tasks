"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
Пример:
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики,
расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3.
И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.
Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
"""

from xml.etree import ElementTree

str_xml = input()
root = ElementTree.fromstring(str_xml)

dict = {'red': 0, "green": 0, "blue": 0}
dict[root.attrib['color']] += 1

def get(root, level=1):
    level += 1
    for child in root:
        dict[child.attrib['color']] += level
        get(child, level)

get(root)
print(dict['red'], dict['green'], dict['blue'])