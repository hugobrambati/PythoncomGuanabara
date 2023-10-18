#Crie um programa que leia 2 notas de um aluno e calcule sua media , mostrando uma mensagem no final de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior :Aprovado

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2


if media < 5.0:
    print('Sua media é {}, você está  REPROVADO'.format(media))
elif media >= 5.0 or media <= 6.9:
    print('Sua média é {}, você esta em RECUPERAÇÂO '.format(media))
else:
    print('Sua média é {}, você esta APROVADO '.format(media))