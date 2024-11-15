#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Exercício 28:

#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# import random
# import time

# nrUsuario = int(input('Informe um número inteiro entre 0 e 5:'))

# numeroPC = random.randint(1, 5)

# print('Processando...')
# time.sleep(3)

# print('O número sorteado foi: {}'.format(numeroPC))

# if nrUsuario == numeroPC:
#     print('Parabéns! Você acertou o número sorteado.')
# else:
#     print('Você errou o número sorteado, tente outra vez. :(')
# print('--FIM do Joguinho--')

import random
import time

nrUsuario = int(input('Informe um número inteiro entre 0 e 10:'))
numeroPc = random.randint(1, 11)
print('O número do PC é:{}'.format(numeroPc))

print('Processando...')
time.sleep(3)

count = 1

while nrUsuario != numeroPc:
    numeroPc = random.randint(1, 11)
    print('O novo número do PC é:{}'.format(numeroPc))   
    count = count + 1
print('A quantidade de tentativas do PC foi de {}x'.format(count - 1))
print('Fim do joguinho!')