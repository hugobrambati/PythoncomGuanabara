#Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o emprestimo será negado.


valorCasa = float(input('Qual o valor do Imovel? R$:'))
salario = float(input("Qual o valor do seu salário? R$: "))
anos = int(input('Em quantos anos pretende pagar?'))


vanual = valorCasa / anos
vmensal = vanual/12

if vmensal < (salario / 100) * 30:
    print('O valor mensal a pagara é de R$: {:.2f}. em {} anos'.format(vmensal, anos))
    print('Emprestimo Concedido')
else:
    print('Para pagar uma casa de R$ : {:.2f}   em {} anos a prestação será de R$:{:.2f}'.format(valorCasa, anos,vmensal))
    print('Emprestimo negado')