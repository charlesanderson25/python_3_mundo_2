# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
count = 0

for c in range(1, 7):
    n = int(input('Informe seis números inteiros:'))
    if n % 2 == 0:
        count = count + 1
        soma = soma + n
    else:
        print('Os números ímpares digitados, serão desconsiderados!')
print('A soma dos {} números pares informados é de: {}'.format(count, soma))