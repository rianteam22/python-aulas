"""
Iteracao: se o elemento tem idices ele eh iteravel
eh o ato de percorrer o elemento iteravel
"""
frase = 'o rato roeu a roupa do rei de roma'
contador = 0
frase2 = ''
print(f'a frase tem {len(frase)} caracteres')
while contador < len(frase):
    frase2 += frase[contador]
    contador += 1
    print(frase2)