"""Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂. 
Определите, можно ли разместить одну из этих коробок внутри другой, при условии, 
что поворачивать коробки можно только на 90 градусов вокруг ребер."""

a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

s1 = sorted([a1, b1, c1])
s2 = sorted([a2, b2, c2])

if s1[0] == s2[0] and s1[1] == s2[1] and s1[2] == s2[2]:
    print("Boxes are equal")
elif s1[0] >= s2[0] and s1[1] >= s2[1] and s1[2] >= s2[2]:
    print("The first box is larger than the second one")
elif s1[0] <= s2[0] and s1[1] <= s2[1] and s1[2] <= s2[2]:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
