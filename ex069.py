# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

stop = 0
count = 0

while True:
    idade = int(input('Informe sua idade:'))
    sexo = str(input('Informe o seu sexo [M/F]:')).strip().upper()[0]

    print('-=' * 25)
    
    if sexo not in ('M', 'F'):
        sexo = str(input('Informe novamente seu sexo, [M] para Masculino ou [F] para feminino:')).strip().upper()[0]

    print('Você deseja continuar? Digite 999 para parar o programa!')

    print('-=' * 30)

    stop = int(input('Informe um número qualquer para continuar ou 999 para parar o programa:'))

    print('-=' * 30)

    if stop == 999:
        print('Você parou o programa!')
        break

    if idade >= 18:
        print('Você é maior de idade!')
        count = count + 1
    else:
        print('Você é menor de idade!')
print(f'A quantidade de pessoas maiores de idade é de {count}')

# NÃO CONCLUÍDO 
# NÃO CONCLUÍDO 
# NÃO CONCLUÍDO 
# NÃO CONCLUÍDO 
# NÃO CONCLUÍDO 