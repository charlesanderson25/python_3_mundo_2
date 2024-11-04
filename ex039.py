#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

anoNascimento = int(input('Informe o ano do seu nascimento:'))

ano_atual = datetime.datetime.now().year

idade = ano_atual - anoNascimento

print('Sua idade é: {} anos!'.format(idade))
print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, ano_atual))

tempoFaltante = 0
passouPrazo = idade - 18

if idade < 18:
    tempoFaltante = 18 - idade
elif idade > 18:
    tempoFaltante = idade - 18

#print('Você deveria ter se alistado há {} anos.'.format(passouPrazo))

if anoNascimento > (ano_atual - 18):
    print('Ainda faltam {} anos para o alistamento'.format(tempoFaltante))
elif anoNascimento == (ano_atual - 18):
    print('Você possui {} anos! Está na idade exata para se alistar'.format(idade))
else:
    print('Você já deveria ter se alistado há {} anos'.format(passouPrazo))


# if idade < 18:
#     print('Quando fizer 18 anos será necessário se alistar no serviço militar!')
# elif idade == 18:
#     print('Você possui a idade exata para alistamento militar obrigatório, aliste-se já!')
# else:
#     print('Já passou do tempo do alistamento militar obrigatório, procure um QG urgente!')