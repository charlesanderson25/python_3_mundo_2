# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = 0
count = 0
soma = 0

while n != 999:
    n = int(input('Informe um número inteiro: '))
    if n == 999:
         break
    count = count + 1
    soma = soma + n
print('-=' * 25)
print(f'A quantidade de números informados foi de: {count}')
print('-=' * 25)
print(f'A soma dos números informados é de: {soma}')
print('-=' * 25)
print('Acabou! Fim')