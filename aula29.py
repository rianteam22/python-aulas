"""
Funcoes em python - *args **kwargs
"""


# Desempacotando a lista
# lista = [1, 2, 3, 4, 5]
# print(*lista, sep='-')

def func(*args, **kwargs):
    # args = list(args)
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    print(kwargs)
    nome = kwargs.get('nome')
    print(nome)
    print(kwargs['sobrenome'])


func(1, 2, 3, 4, 5, nome='rian', sobrenome='galatas')
