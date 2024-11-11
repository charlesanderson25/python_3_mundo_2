# Laços de repetição - Parte 1

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