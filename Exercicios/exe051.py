#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
decimo = num + (10 - 1) * raz 
cont = 0
for c in range (num, decimo + raz, raz):
    print(c)