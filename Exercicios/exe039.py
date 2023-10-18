#Faça um programa que leia o ano de nascimento de um jovem e informe  de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se ja passou do tempo do alistamento

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
dtnsc = int(input('Digite o  ano do seu nascimento: '))

atual = date.today().year
anos = atual - dtnsc

if anos < 18:
    tempoFalta = 18 - anos
    print('Você tem {} anos em {}  e falta {} anos para se alistar'.format(anos, atual, tempoFalta))
elif anos == 18:
    print('Esta na hora de se alistar')
elif anos > 18:
    temp_passado = anos - 18
    print('Você tem {} anos em {} e já se passou {} anos do seu alistamento' .format(anos, atual, temp_passado))

