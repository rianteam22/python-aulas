"""
Listas em python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(f'l1={l1}')
print(f'l2={l2}\n')

l3 = l1 + l2
l4 = l2 + l1

l1.extend(l2) # Concatena
l2.append('a') # Insere no final
print(f'l2={l2}\n')
l1.insert(1, 'b') # Insere no indice
l2.pop() # Retira no final

print(f'l1={l1}')
print(f'l2={l2}\n')
print(f'l3={l3}')
print(f'l4={l4}\n')

del(l3[0:4])

print(f'l3={l3}')
print(f'l4={max(l4)}')
print(f'l4={min(l4)}\n')

l5 = list(range(1, 20))
print(f'l5={l5}')

l6 = list('RIAN GALATAS MACEDO BRANDAO')
print(f'l6={l6}')
print(l6[3])

l7 = ['Rian', 20, 1.66]
print(l7)

