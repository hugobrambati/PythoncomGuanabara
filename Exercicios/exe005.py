#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e o seu antecessor

n1 = int(input('Digite o numero: '))
ant = n1 - 1
suc = n1 + 1

print('O numero digitado foi {}, seu sucessor é {} eo seu antecessor é {}.'.format( n1 , suc, ant))