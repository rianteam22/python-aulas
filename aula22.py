"""
Split Join Enumerate
Split: dividir uma string #str
Join: juntar uma string #str
Enumerate: enumerar elementos de uma lista #iteraveis
"""

string = 'ser legal e legal , mas o tempo todo'
lista1 = string.split(' ')
lista2 = string.split(',')
string2 = ' '.join(lista1)
s1, s2 = lista2
print(lista1, '\n', lista2)
print(string2)
print('strings lista:', s1, s2)

for indice, val in enumerate(lista1):
    print(indice, val)