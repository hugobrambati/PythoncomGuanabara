#faça um programa que leia um angulo qualquer e mostre na tela o valor so seno, coseno e tangente desse angulo

import math
ang = float(input('Digite o angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O angulo foi {:.2f},\n o seno é {:.2f},\n o coseno e {:.2f},\n a tangente é {:.2f}'.format(ang, sen, cos, tang))
