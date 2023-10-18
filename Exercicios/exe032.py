#Faca um programa que leia um ano qualquer e mostre se ele e bissexto.
from datetime import  date
ano = int(input('Qual ano quer analizar? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year #o date esta falando da data de hoje e pegando so o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é  Bissexto!'.format(ano))
else:
    print('O ano {} NÃO é Bissexto!'.format(ano))