#Faça um algoritimo que leia o preço de m produto e mostre seu novo preço com 5% de desconto

preço = float(input('Digite o valor: '))

dsc = preço * 0.05

ttl = preço - dsc

print('O valor do produto é R$: {} com desconto de R$: {} , o valor a pagar e de R$ {}'.format(preço, dsc, ttl))
