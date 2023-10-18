# Crie um programa que leia qnto dinheiro uma pessoa tem n acarteira e mostre qntos dolares e reais ela pode comprar, considere US$1,00 = R$3,27 

real = float(input('Digite o valor em reais: '))
dolar = float(input('Digite o valor da cotação do dolar: '))
euro = float(input('Digite o valor da cotação do euro: '))

cd = real/dolar
ce = real/euro

print("Você tem R$: {} e pode comprar US$: {:.4} ". format(real, cd))
print("Você tem R$: {} e pode comprar €: {:.4} ". format(real, ce))


