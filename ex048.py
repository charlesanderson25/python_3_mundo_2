# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
count = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        count = count + 1
        soma = soma + c
print('A soma de todos os {} números ímpares e múltiplos de 3 entre 1 e 500 é de: {}'.format(count, soma))