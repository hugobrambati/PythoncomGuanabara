#Crie uma programa que leia o nome da sua cidade e diga se ela começa ou não com "SANTO". 

cidade = str(input('Em qual cidade você nasceu? ')).strip()#retirar espaços da frente e de tras

print(cidade[:5].lower() == 'santo')#pegou a variavel definio as 4 primeiras posições, jogou para maiuscula e comparou a variavel


