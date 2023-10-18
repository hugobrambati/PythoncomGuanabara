#Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimitros

m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = m * 1000

print('Você digitou {} metros e ele tem \n {} centimetros \n {} milimetros'.format( m, cm, mm))