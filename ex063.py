#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)

n = int(input('Quantos termos deseja mostrar?'))
primeiro = 0
segundo = 1

print('{} > {}'.format(primeiro, segundo), end='')

count = 3

while count <= n:
    terceiro = primeiro + segundo
    print(' > {}'.format(terceiro), end='')
    primeiro = segundo
    segundo = terceiro
    count = count + 1
print(' > Fim')


# NÃO CONCLUÍDO!
# NÃO CONCLUÍDO!
# NÃO CONCLUÍDO!
# NÃO CONCLUÍDO!
# NÃO CONCLUÍDO!
