"""
 esturtura de repeticao FOR
 iterando com FOR
 Funcao range (start=0, stop, step=1)
"""

# continue - pula para o proximo laco
# break - termina o laco

texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)
print('')

# ////////////////////////////////////////////////////

for n in range(1, 20, 1):
    print(n)
print('')
for n in range(0, 100, 3):
    print(n)
print('')
for n in range(100):
     if n % 3 == 0:
        print(n)
