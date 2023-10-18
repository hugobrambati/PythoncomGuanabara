#Elabore um programa que calcule o valor ser pago por um produto considerando o seu preço normal e condição de pagamento:
#á vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#2 x no cartão preço normal
# 3x ou mais no cartão juros de 20%

preco = float(input('Digite o preço do produto: '))
conpg = int(input('Digite: 1 - Avista (dinheiro  ou cheque)\nDigite: 2 -À vista (Cartão)\nDigite: 3 - Parcelado em 2X\nDigite: 4 - Parcela em 3x ou mais :'))

if conpg == 1:
    desc = (preco/100) * 10
    totalProduto = preco - desc
    print('O valor do produto é R$ {:.2f}\nA forma de pagamento {}\nValor do Desconto R${:.2f}\nTotal a pagar R$ {:.2f}'.format(preco, conpg, desc, totalProduto))
elif conpg == 2:
    desc = (preco/100)*5
    totalProduto = preco - desc
    print('O valor do produto é R$ {:.2f}\nA forma de pagamento {}\nValor do Desconto R${:.2f}\nTotal a pagar R$ {:.2f}'.format( preco, conpg, desc, totalProduto))
elif conpg == 3:
    parc =  preco / 2
    print('O valor do produto é R$ {:.2f}\nA forma de pagamento {}\nTotal a pagar R$ {:.2f}\nParcelado em duas vezes de R$: {:.2f}'.format(preco, conpg,preco,parc))
elif conpg == 4:
    juros = (preco/100)*20
    tprod = preco + juros
    print('O valor do produto é R$ {:.2f}\nA forma de pagamento {}\n Acrescimo de juros de R$: {:.2f}\n Total a pagar R$ {:.2f}'.format(preco, conpg,juros,tprod))
else:
    print('Codigo invalido')
