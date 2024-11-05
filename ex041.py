# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

import datetime

anoNascimento = int(input('Atleta: Informe o ano do seu nascimento:'))

anoAtual = datetime.datetime.now().year

print('Ano atual: {}'.format(anoAtual))

idade = anoAtual - anoNascimento

print('Sua idade é de: {} anos'.format(idade))

if idade < 9:
    print('Atleta: Sua categoria é a MIRIM!')
if idade >= 9 and idade < 14:
    print('Atleta: Sua categoria é a INFANTIL!')
elif idade >= 14 and idade < 19:
    print('Atleta: Sua categoria é a JÚNIOR!')
elif idade >= 19 and idade < 25:
    print('Atleta: Sua categoria é a SÊNIOR!')
elif idade >= 25:
    print('Atleta: Sua categoria é a MASTER!')