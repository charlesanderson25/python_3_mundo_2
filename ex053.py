#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Informe uma frase qualquer:'))

minusculas = frase.lower()

deleteSpaces = minusculas.strip()
deleteSpaces1 = deleteSpaces.replace(" ", "")

print('A frase sem espaços: {}'.format(deleteSpaces1))

if deleteSpaces1 == deleteSpaces1[::-1]:
    print('A frase informada: -_{}_- é um palíndromo!'.format(deleteSpaces1))
else:
    print('A frase informada: -_{}_- não é um palíndromo!'.format(deleteSpaces1))