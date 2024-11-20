# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0

while True:
    n = int(input('Informe um número inteiro para saber sua tabuada: '))

    if n < 0:
        break

    print('-=' * 20)

    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')

print('-=' * 25)

print('PROGRAMA TABUADA ENCERRADO!')