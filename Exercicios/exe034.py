# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%

salario = float(input("Digite seu salario: "))

if salario >= 1250:
    primeiroaumentoSalario = (salario / 100) * 10
    print('O seu salario atual é de R$ {:.2f}.'.format(salario))
    print('O aumento foi de R$: {:.2f}'.format(primeiroaumentoSalario))
    print('O proximo salário vai ser de R$: {:.2f}'.format(salario + primeiroaumentoSalario))
else:
    segundoAumentoSalario = (salario / 100) * 15
    print('O seu salario atual é de R$ {:.2f}.'.format(salario))
    print('O aumento foi de R$: {:.2f}'.format(segundoAumentoSalario))
    print('O proximo salário vai ser de R$: {:.2f}'.format(salario + segundoAumentoSalario))
