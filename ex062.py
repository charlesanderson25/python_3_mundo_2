#  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

p1 = int(input('Informe o primeiro termo da Progressão Aritmética(PA):'))
razao = int(input('Informe a razão da Progressão Aritmética(PA):'))

print('O primeiro termo da razão é: {}'.format(p1))
print('A razão é: {}'.format(razao))

c = 1
count = 0

while c < 11:
    termo = p1 + c * razao
    print(termo)
    c = c + 1
    
    demaisTermos = int(input('Quantos termos você deseja mostrar a mais?'))
    if demaisTermos != 0:
        termo = demaisTermos + c * razao
        print(termo)
        count = count + 1
    else:
        print('Progressão finalizada com {} termos mostrados!'.format(count))
print('ACABOU!')

# NÃO CONCLUÍDO! 
# NÃO CONCLUÍDO! 
# NÃO CONCLUÍDO! 
# NÃO CONCLUÍDO! 
# NÃO CONCLUÍDO! 
