# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

num1 = float(input('Informe o primeiro número:'))
num2 = float(input('Informe o segundo número:'))

if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior:')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')

