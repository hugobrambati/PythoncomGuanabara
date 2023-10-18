# Escreva um programa que leia a velocidade de um carro.
#Se ele ultapassr 80km/h, mostre uma mensagem dizendo que le foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite


vlc = int(input('Digite a velocidade registrada: '))

dif_vlc = vlc - 80

#print(dif_vlc)

if vlc > 80:
    multa = dif_vlc * 7
    print('A velocidade registrada é de {} km/h.'.format(vlc))
    print('Você passou a {} km/h a cima da velocidade e vai recer uma multa de  R$:{},00'. format(dif_vlc,multa))
else:
    print('Tenha um bom dia e dirija com segurança')