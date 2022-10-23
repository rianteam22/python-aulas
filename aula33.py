"""
- Sets em Python (Conjuntos) -
- add
- update
- clear
- discard
- union -> |
- insersection -> &
- diference -> - (elementos presentes apenas no set da esquerda)
- symetric_difference -> ^
"""

s1 = {1, 2, 3, 4, 5, 6, 7}

s2 = set()
s2.add(1)
s2.add(2)
s2.discard(2)
s2.update('riangalatas')

print(s2)