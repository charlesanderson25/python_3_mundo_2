# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idades = []
count = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20_anos = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Informe seu nome:'))
    idade = float(input('Informe sua idade:'))
    sexo = str(input('Informe (M) para sexo masculino e (F) para sexo feminino:'))
    idades.append(idade)
    count = count + 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20_anos = mulheres_menos_20_anos + 1
        

    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
        

print('Existem {} mulheres com menos de 20 anos na lista.'.format(mulheres_menos_20_anos))
print('O nome do homem mais velho é {} com {} anos'.format(nome_homem_mais_velho, idade_homem_mais_velho))
somaIdades = sum(idades)
mediaIdades = somaIdades / count
print('A média das idades é de: {}'.format(mediaIdades))


    