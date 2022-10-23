"""
Formatando valores com modificadores
:s - texto(string)
:d - inteiros(int)
:f - ponto flutuante(float)
:.(numero)f - quantidade de casas decimais(float)
:(caractere)(< ou > ou ^)(quantidade)(tipo - s, d ou f)

< - direita
> - esquerda
^ - centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
