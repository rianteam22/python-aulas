"""
Expressões lambda (funções anônimas) em Python
"""

a = lambda x, y: x * y
print(a(2,2))


lista = [['p1', 10], ['p2', 3], ['p3', 5], ['p4', 51], ['p5', 8]]

lista.sort(key=lambda item: item[1])
print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
