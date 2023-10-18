#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt,pow

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

"""rco = pow(co ,2)
rca = pow(ca, 2)

t_raiz = rco + rca

h = sqrt(t_raiz)"""

h = sqrt(pow(co,2) + pow(ca,2))

print('O coprimento da hipotenusa e {:.2f}'.format(h))
