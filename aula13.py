# Estrutura de repetição for

for c in range(1, 6):
    print('Estrutura de repetição está on!')
print('FIM!')

######################################################

for c in range(1, 6):
    print(c)
print('FIM!')

######################################################

for c in range(6, 0, -1): #contar para trás
    print(c)
print('FIM!')

######################################################

for c in range(1, 6, 2): # pular de 2 em 2 
    print(c)
print('FIM!')

######################################################

n = int(input('Informe um número até 9:'))

for c in range(1, n):
    print(c)
print('FIM!')

######################################################

i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))

for c in range(i, f+1, p):
    print(c)
print('FIM!')

######################################################

for c in range(0, 3):
    n = int(input('Digite um valor 3x:'))
    print(n)
print('FIM!')

######################################################

s = 0

for c in range(0, 4):
    n = int(input('Informe um número inteiro até 9:'))
    s = s + n
print('O somatório dos valores informados é de {}'.format(s))
print('FIM!!')

# Laços de repetição - Parte 2

for c in range(1, 6):
    print('Oi')
print('FIM')

#-------------------------------------------------#

for c in range(1, 6):
    print(c)
print('FIM')

#-------------------------------------------------#

for c in range(6, 0):
        print(c)
print('FIM')

#-------------------------------------------------#

for c in range(6, 0, -1):
        print(c)
print('Fim')

#-------------------------------------------------#

for c in range(0, 6, 2):
        print(c)
print('Fim')

#-------------------------------------------------#

n = int(input('Digite um número:'))
for c in range(0, n + 1):
    print(c)
print('FIM')
    
#-------------------------------------------------#

i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))

for c in range(i, f, p):
      print(c)
print('FIM!!!')