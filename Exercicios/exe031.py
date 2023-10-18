#Desenvolva um programa que pergunte a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagem ate 200 km e R$ 0,45 para viagens mais longas
km = float(input('Digite a distancia a percorrer :'))

if km <= 200:
    valor = km * 0.50

    print('O valor total da viagem e de R$: {:.2f}'.format(valor))
else:
    valor = km * 0.45
    print('O valor total da viagem e de R$: {:.2f}'.format(valor))
