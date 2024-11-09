# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 

p1 = int(input('Informe o primeiro termo da Progressão Aritmética(PA):'))
razao = int(input('Informe a razão da Progressão Aritmética(PA):'))

print('O primeiro termo da razão é: {}'.format(p1))
print('A razão é: {}'.format(razao))

for c in range(1, 10):
    termo = p1 + c * razao
    print(termo)
print('ACABOU!')




