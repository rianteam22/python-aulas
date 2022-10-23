"""
List Comprehension em Python
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [var for var in l1]
l3 = [var * 2 for var in l1]
l4 = [(var, var2) for var in l1 for var2 in range(3)]

l5 = ['Rian', 'Adel', 'Marcs']
l6 = [var.replace('a', '$').upper() for var in l5]

l7 = list(range(100))
l8 = [var for var in l7 if var % 3 == 0]
print(l8)