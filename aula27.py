"""
Funcoes def em python
"""


def massinha(massage='mago', nome='fraco'):
    nome = nome.replace('e', '***')
    print(massage, '\n', nome)
    return f'{massage} {nome}'


msg = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'
massinha(massage='fernando')
massinha('RIAN', 'GALATAS')
massinha(nome='marcos')
massinha(massage=msg, nome=msg)
massinha(nome=msg, massage=msg)
print(massinha())