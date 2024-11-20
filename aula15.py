# Laços de Repetição - Interrompendo repetições While

n = 0
soma = 0

while True:
    n = int(input('Informe um número inteiro:'))
    if n == 999:
        break
    soma = soma + n
# print('A soma dos números informados é de: {}'.format(soma))
print(f'A soma dos números informados é de: {soma}')
