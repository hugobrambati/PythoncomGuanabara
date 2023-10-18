#Crie um programa que leia o nome de uma pessoa e diga se ela tem o "SILVA" no nome.

nome = str(input('Digite seu nome: ')).strip()

print('Seu nome tem Silva ? {}'.format('SILVA' in nome.upper()))#aqui analisa se existe SILVA na variavel nome jogando nome para maisculo

