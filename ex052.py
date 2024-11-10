# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro:'))

count = 0

for c in range(1, n + 1): # O ' + 1 ' no final é porque no Python conta-se sempre -1 no range() do for. 
    if n % c == 0:
        print('\033[33m', end='')
        count = count + 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

if count == 2:
    print('O número {} foi divisível {} vezes.'.format(n, count))
    print('\n\033[mO número {} é primo!'.format(n))
else:
    print('O número {} foi divisível {} vezes.'.format(n, count))
    print('\n\033[mO número {} não é primo!'.format(n))