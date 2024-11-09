# Tabuada

n = int(input('Digite um número para ver sua tabuada:'))

for c in range(1, 11):
    tabuada = n * c
    print('{} X {:2} = {}'.format(n, c, tabuada))