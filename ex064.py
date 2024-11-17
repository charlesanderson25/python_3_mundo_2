# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n1 = 0
count = 0
soma = 0

while n1 != 999:
    n1 = int(input('Informe um número inteiro: [999 para parar]'))
    print('O número informado é {}'.format(n1))
    
    if n1 != 999:
        soma = soma + n1
        count = count + 1
        
print('-=' * 22)
print('A quantidade de números informados foi de {} e sua soma é de: {}'.format(count, soma))
print('-=' * 22)
print('Fim do programa!')


# n2 = int(input('Informe outro número inteiro:'))
# n3 = int(input('Informe mais um número inteiro:'))

