# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# Exercício 51:

# # Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 

# p1 = int(input('Informe o primeiro termo da Progressão Aritmética(PA):'))
# razao = int(input('Informe a razão da Progressão Aritmética(PA):'))

# print('O primeiro termo da razão é: {}'.format(p1))
# print('A razão é: {}'.format(razao))

# for c in range(1, 10):
#     termo = p1 + c * razao
#     print(termo)
# print('ACABOU!')

p1 = int(input('Informe o primeiro termo da Progressão Aritmética(PA):'))
razao = int(input('Informe a razão da Progressão Aritmética(PA):'))

print('-=' * 12)

print('O primeiro termo da razão é: {}'.format(p1))
print('A razão é: {}'.format(razao))

c = 1

while c <= 10:
    termo = p1 + c * razao
    print(termo)
    c = c + 1
print('ACABOU!')