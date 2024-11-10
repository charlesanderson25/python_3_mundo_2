# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro:'))

if n / 1 == n and n / n == 1:
    print('O número {} é um número primo!'.format(n))
else:
    print('O número {} NÃO é primo!'.format(n))