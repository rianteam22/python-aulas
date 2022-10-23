"""
Condicional com o operador OR
"""

nome = input('Nome: ')
# ira parar na primeira expressao verdadeira
print(nome or None or False or 0 or 'voce nao digitou nada')