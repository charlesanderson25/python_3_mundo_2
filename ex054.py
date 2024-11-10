#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

anoAtual = datetime.datetime.now().year

for c in range(1, 8):
    anoNascimento = int(input('Informe seu ano de nascimento:'))
    print('Seu ano de nascimento é: {}'.format(anoNascimento))
    idade = anoAtual - anoNascimento
    print('Sua idade é de: {} anos'.format(idade))
    if idade >= 18:
        print('Você já atingiu a maioridade!')
    else:
        print('Você ainda não atingiu a maioridade!')