# Faça um programa que leia um numero inteiro e digoa se ele é ou não um numero primo.

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')    
    print('{}\n'.format(c), end='')
print(tot)