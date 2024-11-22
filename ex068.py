# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('-=' * 25)
print('Vamos jogar PAR ou ÍMPAR')
print('-=' * 25)

jogador = int(input('Digite um valor:'))

escolha = str(input('PAR ou ÍMPAR?  [P/I]: ')).upper()

computador = random.randint(1, 1000)

total = jogador + computador

if total % 2 == 0:
    resultadoPar = 'DEU PAR'
else:
    resultadoImpar = 'DEU ÍMPAR'

# if escolha == resultadoPar:
#     vitoriaDerrota = 'Você VENCEU!'
# elif escolha == resultadoImpar:
#     vitoriaDerrota = 'Você PERDEU!'

print(f'Você jogou {jogador} e o computador {computador}. Total de {total} {resultado}')

print('-=' * 25)

print(vitoriaDerrota)

print('-=' * 25)

print('GAME OVER')