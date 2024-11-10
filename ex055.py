# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for c in range(1, 6):
    peso = float(input('Informe seu peso em Kg:'))
    print('Seu peso é de {} Kg'.format(peso))
    pesos.append(peso)

peso_maximo = max(pesos)
peso_minimo = min(pesos)
print('O maior peso é de {} Kg'.format(peso_maximo))
print('O menor peso é de {} Kg'.format(peso_minimo))