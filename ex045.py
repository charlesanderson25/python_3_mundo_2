# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

print('''Suas opções:
      
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
      ''')

jogador = int(input('Qual sua jogada?'))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO! ! !')
time.sleep(1)

computador = random.randint(0, 2)

if jogador == 0 and computador == 1:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador VENCE!')
elif jogador == 0 and computador == 2:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou TESOURA')
    print('Jogador jogou PEDRA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Jogador VENCE!')
elif jogador == 1 and computador == 0:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PEDRA')
    print('Jogador jogou PAPEL')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Jogador VENCE!')
elif jogador == 1 and computador == 2:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador VENCE!')    
elif jogador == 2 and computador ==0:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador VENCE!')
elif jogador == 2 and computador == 1:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PAPEL')
    print('Jogador jogou TESOURA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Jogador VENCE!')
elif jogador == 0 and computador == 0:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PEDRA')
    print('Jogador jogou PEDRA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE!')
elif jogador == 1 and computador == 1:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou PAPEL')
    print('Jogador jogou PAPEL')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE!')
elif jogador == 2 and computador == 2:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Computador jogou TESOURA')
    print('Jogador jogou TESOURA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE!')
else:
    print('JOGADA INVÁLIDA!')



