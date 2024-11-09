# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

print('Preparado para ver os fogos? ? ?')

for c in range(0, 11):
    if c == 0:
        print('Dez...')
        time.sleep(1)
    elif c == 1:
        print('Nove...')
        time.sleep(1)
    elif c == 2:
        print('Oito...')
        time.sleep(1)
    elif c == 3:
        print('Sete...')
        time.sleep(1)
    elif c== 4:
        print('Seis...')
        time.sleep(1)
    elif c == 5:
        print('Cinco...')
        time.sleep(1)
    elif c == 6:
        print('Quatro...')
        time.sleep(1)
    elif c == 7:
        print('Tres...')
        time.sleep(1)
    elif c == 8:
        print('Dois...')
        time.sleep(1)
    elif c == 9:
        print('Um...')
        time.sleep(1)
    elif c == 10:
        print('BOOOOOMMM...!!!')
        