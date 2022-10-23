"""
Dicionários em Python - uma ED que suporta um par de chave e valor
o valor de cada chave eh unico
pode usar qualquer tipo de dado imutavel
"""

d1 = {'chave' : 'valor da chave'}

d1['nova_chave'] = 'valor da nova_chave'

d2 = dict(chave2='val')

print(d1)
print(d1['chave'])
print(d2)
print('\n')

for v in d1.values():
    print(v)
