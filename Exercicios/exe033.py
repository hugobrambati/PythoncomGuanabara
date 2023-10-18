#Faça um programa  que leia 3 numeros e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite primeiro numero: '))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input('Digite o terceiro numero: '))

#Verificando o menor
menor = n1

if n2 <  n1 and n2< n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2 > n1 and n3>n2:
    maior = n1
if n3>n1 and n3>n2:
    maior = n3

print('O menor numero e {} é o maior numero é {}'.format(menor, maior))

