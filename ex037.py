#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Informe um número inteiro:'))

print('[1] Para conversão em binário')
print('[2] Para conversão em octal')
print('[3] Para conversão em hexadecimal')

escolha = int(input('Informe a base para conversão:'))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if escolha == 1:
    print('O número {} em binário é: {}'.format(numero, binario))
elif escolha == 2:
    print('O número {} em octal é: {}'.format(numero, octal))
elif escolha == 3:
    print('O número {} em hexadecimal é: {}'.format(numero, hexadecimal))
else:
    print('Escolha inválida, tente novamente!')
