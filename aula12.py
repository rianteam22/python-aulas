"""
operadores logicos
and, or, not, in, not in

'' - considerado falso
0 - considerado falso
"""
comparacao1 = False
comparacao2 = True

print(comparacao1 and comparacao2)

print(comparacao1 or comparacao2)

print(not comparacao1 and not comparacao2)

nome = 'Rian Galatas'

if 'R' in nome:
    print('tem')
if 'Gala' not in nome:
    print('nao tem Gala')
else:
    print('tem Gala')
