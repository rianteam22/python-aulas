"""
Tuplas em Python
tuplas nao alteram o valor do indice
tem q ser transformado em lista
"""

t1 = (1, 2, 3, 4, 'a', 'Rian Galatas')

print(type(t1), f'\n{t1}')

t1 = list(t1)
t1[1] = 200
t1 = tuple(t1)

print(t1)
