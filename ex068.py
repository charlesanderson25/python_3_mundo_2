# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

vitoria = 0

print('-=' * 25)
print('Vamos jogar PAR ou ÍMPAR')
print('-=' * 25)

while True:

    jogador = int(input('Digite um valor:'))

    escolha = str(input('PAR ou ÍMPAR?  [P/I]: ')).strip().upper()[0]

    while escolha not in ('P', 'I'):
        escolha = input('Informe novamente uma opção [P] para PAR ou [I] para ímpar!').strip().upper()[0]

    computador = random.randint(1, 1000)

    total = jogador + computador

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

    if total % 2 == 0:
        print('DEU PAR!')
    else:
        print('DEU ÍMPAR!')

    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria =  vitoria + 1
        else:
            print('Você PERDEU!')
            break

    if escolha == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitoria = vitoria + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {vitoria} vezes!')
print('GAME OVER!')