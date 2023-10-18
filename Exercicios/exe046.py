#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com pausas de 1 segundo entre eles.

from time import sleep#funcionalidade de contagem de tempo

for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print('POW, POW, BUM')
