 #Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Informe o valor da casa que pretende adquirir R$:'))
salario = float(input('Informe o valor do seu salário mensal R$:'))
anosPagamento = int(input('Informe a quantidade de anos que pretende quitar o financiamento:'))

mesesPagamento = anosPagamento * 12

prestacao = valorCasa / mesesPagamento

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(valorCasa, anosPagamento, prestacao))

if prestacao > salario * 30 / 100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
