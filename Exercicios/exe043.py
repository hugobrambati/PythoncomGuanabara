#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seus status, de acordo com a tabela abaixo
#Abaixo de 18.5: abaixo do peso.
##Entre 18.5 e 25 : Peso ideal
#entre 25 ate 30 : Sobrepeso
#30 até 40 : Obesidade
#acima de 40: Obeseidade Morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso /(altura**2)

if imc < 18.5:
    print('Seu IMC esta {:.1f} , ele se enconta Abaixo do Peso'.format(imc))
elif imc >= 18.5 and  imc < 25:
    print('Seu IMC esta {:.1f} , ele se enconta no Peso Ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC esta {:.1f} , ele se enconta no Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC esta {:.1f} , ele se enconta em Obesidade'.format(imc))
else:
    print('Seu IMC esta {:.1f} , ele se enconta em Obesidade Morbidal'.format(imc))