#Escreva um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro numero é maior
#O Segundo numero é o maior
#Não existe numero valor maior , os dois são iguais

a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))


if a > b:
    print('O primeiro numero é o maior')
elif b > a:
    print('O segundo numero é maior ')
else:
    print('Não existe valor maior, os dois são iguais')