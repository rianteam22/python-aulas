"""
Criar variaveis para nome, idade
altura e peso
Criar variavel com o ano atual
Obter o ano de nascimento de uma pessoa
Exibir um texto com todos os valores na tela usando F-Strings
"""

nome = 'Rian'
idade = 20
altura = 1.66
peso = 90
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos no ano de {ano_atual}, nasceu em {ano_nascimento}. Pesa {peso}Kg com {altura}m. Seu IMC eh {imc:.2f}')