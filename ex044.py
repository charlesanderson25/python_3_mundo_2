#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Informe o valor do produto em R$:'))

dinheiroCheque = valorProduto - (valorProduto * 0.10)
cartao = valorProduto - (valorProduto * 0.05)
cartao2x = valorProduto / 2

cartao3x = ((valorProduto * 0.20) + valorProduto) / 3

print('Para pagamento em dinheiro ou cheque o valor será de R$: {:.2f}'.format(dinheiroCheque))

parcelas = int(input('Para pagamentos parcelados no cartão, informe a quantidade de parcelas:'))

if parcelas == 1:
    print('Para pagamento em 1x no cartão o valor será de R$: {:.2f}'.format(cartao))
elif parcelas == 2:
    print('Para pagamento em 2x no cartão o valor será de 2x R$: {:.2f}'.format(cartao2x))
elif parcelas >= 3:
    print('Para pagamento em 3x no cartão o valor será de 3x R$: {:.2f}'.format(cartao3x))

