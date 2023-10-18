# A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# - Até 9 anos : Mirim
# - até 14 anos : Infantil
# até 19 anos : Junior
# até 20 anos : Senior
# Acima : Master

from datetime import  date
ntnasc = int(input('Digite  data de nascimento do atleta: '))

anoatual = date.today().year
anos = anoatual - ntnasc

if anos <= 9:
    print("O atleta tem {} anos e sua categoria é Mirim".format(anos))
elif (anos > 9) and (anos <= 14):
    print("O atleta tem {} anos e sua categoria é Infantil".format(anos))
elif (anos > 14) and (anos <= 19):
    print("O atleta tem {} anos e sua categoria é Junior".format(anos))
elif (anos > 19) and (anos == 20):
    print("O atleta tem {} anos e sua categoria é Senior".format(anos))
else:
    print("O atleta tem {} anos e sua categoria é Master".format(anos))
