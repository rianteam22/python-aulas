"""
Operadores relacionais - ==, >, >=, <, <=, !=
"""
# nome = input('Nome: ')
idade = int(input('Idade: '))

jovem = 20
velho = 30

if jovem <= idade <= velho:
    print(f'pode pegar o emprestimo')
else:
    print(f'NAO pode pegar o emprestimo')