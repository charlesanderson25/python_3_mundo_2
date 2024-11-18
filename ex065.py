# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
count = 0
soma = 0
maior = 0
menor = 0

while n != 999:
    n = int(input('Informe números inteiros [999 para parar]:'))
    print('O número informado é: {}'.format(n))

    if n != 999:
        count = count + 1
        soma = soma + n
    
    if count == 1 and n != 999:
        maior = menor = n
    elif n != 999:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
media = soma / count

print('-=' *20)
print('O valor de count é de {}'.format(count))
print('-=' *20)
print('O valor da soma é de: {}'.format(soma))
print('-=' *20)
print('O valor da média é de: {}'.format(media))
print('-=' *20)
print('O maior número informado é {}, e o menor número informado é {}'.format(maior, menor))
print('-=' *20)

print('FIM!')
