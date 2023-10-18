#Escreva um programa que faça o computador "pensar'' em um numero inteiro entre 0 e 5e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
import random

num = random.randint(0,5)

nsort =  num

print(num)

print("Tente adivinhar um numero de 1 ate 5")
chute = int(input("De seu palpite: "))

if chute == nsort:
    print('Parabens acertou !')
else:
    print('Não foi dessa vez, eu pensei no {} e voce chutou o {}.'.format(nsort, chute))
