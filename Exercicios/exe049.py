##refaça um programa que leia um numero Inteiro qualquer e mostre na tela sua tabuada

n = int(input("Digite qual tabuada vc quer saber: "))
for c in range(0, 11, 1):
    m = n * c
    print('{} X {} = {}'.format(n, c, m))

