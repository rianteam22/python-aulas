"""
For / Else
else sera executado caso a execucao saia do laco antes dele acabar
"""

lista = ['Rian', 'Galatas', 'Macedo']

for valor in lista:
    if valor.startswith('R'):
        print('comeca com r', valor)
    else:
        print('nao comeca com r')