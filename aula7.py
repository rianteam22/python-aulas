"""
F-Strings
"""
nome = 'RIan'
idade = 20
altura = 1.665234256236
print(f'{nome} tem {idade} anos de idade e {altura} de altura')
print(f'{nome} tem {idade} anos de idade e {altura:.2f} de altura')
print('{} tem {} anos de idade e {:.2f} de altura'.format(nome, idade, altura))
print('{2:.2f}  {0}  {1}  {0}  {2:.2f} {1} '.format(nome, idade, altura))
