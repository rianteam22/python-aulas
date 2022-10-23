usuario = input('Digite seu usuario: ')
qtd_char = len(usuario)
print(usuario, qtd_char, type(qtd_char), usuario.__len__())

if qtd_char < 6:
    print('Quantidade incorreta de caracteres')
else:
    print('Voce foi cadastrado')