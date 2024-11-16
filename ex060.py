# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# n = int(input('Informe um número inteiro qualquer:'))

# if n != 0:
#     fatorial = (n * (n - 1)) * (n - 2) * (n - 3) * (n - 4)
# print('O fatorial do número informado é: {}'.format(fatorial))

import math

n = int(input('Informe um número inteiro qualquer:'))

print('O fatorial do número informado é: {}'.format(math.factorial(n)))

