# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

# Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Informe o tamanho da primeira reta:'))
b = float(input('Informe o tamanho da segunda reta:'))
c = float(input('Informe o tamanho da terceira reta:'))

if a + b > c and a + c > b and b + c > a:
    print('Todas condições atendidas, essas retas podem formar um triângulo!')
    if a == b and a == c:
        print('Triângulo EQUILÁTERO!')
    elif (a == b) or (b == c):
        print('Triângulo ISÓSCELES!')
    elif a != b and a != c and b != c:
        print('Triângulo ESCALENO!')
else:
    print('\033[31mUma ou mais condições não foram atendidas, essas retas não podem formar um triângulo!')

