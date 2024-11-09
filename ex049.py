# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# DESAFIO 009: Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

t1 = 1
t2 = 2
t3 = 3
t4 = 4
t5 = 5
t6 = 6
t7 = 7
t8 = 8
t9 = 9
t10= 10

n = int(input('Informe um número inteiro entre 1 e 9:'))

for c in range(1, 10):    
    tab1 = t1 * n
    tab2 = t2 * n
    tab3 = t3 * n
    tab4 = t4 * n
    tab5 = t5 * n
    tab6 = t6 * n
    tab7 = t7 * n
    tab8 = t8 * n
    tab9 = t9 * n
    tab10 = t10 * n
print('A tabuada de {} é:'.format(n))
print('{} X {} é: {}'.format(n, t1, tab1))
print('{} X {} é: {}'.format(n, t2, tab2))
print('{} X {} é: {}'.format(n, t3, tab3))
print('{} X {} é: {}'.format(n, t4, tab4))
print('{} X {} é: {}'.format(n, t5, tab5))
print('{} X {} é: {}'.format(n, t6, tab6))
print('{} X {} é: {}'.format(n, t7, tab7))
print('{} X {} é: {}'.format(n, t8, tab8))
print('{} X {} é: {}'.format(n, t9, tab9))
print('{} X {} é: {}'.format(n, t10, tab10))