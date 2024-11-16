# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

import time

n1 = int(input('Informe o primeiro número:'))
n2 = int(input('Informe o segundo número:'))

escolha = 0

while escolha != 5:

    print('Escolha uma opção abaixo:')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')

    escolha = int(input('Qual sua opção?'))

    if escolha == 1:
        soma = n1 + n2
        print('A soma dos números é igual à: {}'.format(soma))
    elif escolha == 2:
        multiplicacao = n1 * n2
        print('O resultado da multiplicação dos números é: {}'.format(multiplicacao))
    elif escolha == 3:
        if n1 > n2:
            print('O número {} é o maior valor'.format(n1))
        else:
            print('O número {} é o maior valor'.format(n2))
    elif escolha == 4:
        n1 = int(input('Informe o primeiro número:'))
        n2 = int(input('Informe o segundo número:'))
    elif escolha == 5:
        print('Encerrando o programa. . .')
        time.sleep(2)
        print('F-I-M   D-O   P-R-O-G-R-A-M-A!')

print('Programa encerrado!')