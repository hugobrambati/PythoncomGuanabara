#Escreva um programa que pergunte a quantidade de KM percorrido por um carro e a qntidade de dias pelos quais foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60,00por dia R$0,15 por kilometro rodado

dtinicial = int(input('Digite o dia da retirada do carro: '))
kminicial = float(input('Digite a km do carro na retirada: '))
dtfinal = int(input('Digite o dia da devolução do carro: '))
kmfinal = float(input('Digite a km do carro da devolução: '))
dalugado = dtfinal-dtinicial
custoDiario = dalugado * 60.00
kmrodados = kmfinal-kminicial
custoKm = kmrodados * 0.15

cta = custoDiario + custoKm

print('Data do aluguel {} de Outubro'.format(dtinicial))
print('Data da devolução {} de Outubro\n'.format(dtfinal))
print('Km Inicial: {}'.format(kminicial))
print('Km Final: {}'.format(kmfinal))
print('Dias de aluguel: {}'.format(dalugado))
print('Km rodados no periodo: {}\n'.format(kmrodados))
print('Valor das diarias, R$ {}'.format(custoDiario))
print('Valor da Km usado, R$:{}'.format(custoKm))
print('Valor total a apagar R$: {}'.format(cta))



