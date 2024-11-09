# Crie um programa que mostre na tela todos os números pares que estão no intevalo entre 1 e 50.

print('Esses são os números pares entre 1 e 50:')

for c in range(1, 51):
    if c % 2 == 0:
        print(c)
print('FIM!!!')

#----------------------------------------------------

# Forma mais performática de fazer:

print('Esses são os números pares entre 1 e 50:')

for c in range(2, 51, 2):
    print(c)
print('FIM!!!')