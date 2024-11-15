# Estrutura de repetição While

# Conhecendo o limite, pode-se utilizar tanto o For quano o While 

# Usando o For

for c in range(1, 5):
    print(c)
print('FIM do For!')

# Usando o While

c = 1
while c < 5:
    print(c)
    c = c + 1
print('FIM do While!')

# Quando o limite é desconhecido, utiliza-se o While

n = 1
while n != 0:
    n= int(input('Informe um número inteiro:'))
print('FIM do teste com While')

##############################################################################

teste = 'S'
while teste == 'S':
    numero = int(input('Digite um número inteiro:'))
    teste = input('Deseja continuar? [S] ou [N]?:').upper()
print('Fim do teste com while')

##############################################################################

n1 = 1
par = 0
impar = 0
while n1 != 0:
    n1 = int(input('Digite um valor:'))
    if n1 != 0:
        if n1 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

