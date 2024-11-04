# Estruturas condicionais aninhadas

nome = str(input('Informe seu primeiro nome:'))

if nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome == 'Pedro' or nome == 'Tiago' or nome == 'Lucas':
    print('Seu nome também é bastante popular!')
elif nome in 'Paula, Jéssica, Jade, Jude, Milena':
    print('Olá {}, Tens um belo nome feminino!'.format(nome))
else:
    print('Olá {}, talvez seu nome não seja tão popular!'.format(nome))