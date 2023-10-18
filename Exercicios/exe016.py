#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela  sua porção inteira 
# EX: Digitado o numero 6.127. O numero digitado 6.127 tem a parte inteira 6. 

from math import floor

n = float(input("Digite um numero: "))
print('O numero digitado foi {} e tem a parte inteira {}.'.format(n, floor(n))



