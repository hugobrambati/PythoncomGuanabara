"""Crie um programa que leia o nome completo de uma pessoa e mostre:
    *O nome com todas as letras maiuscula
    *O nome com todas as letras minuscula
    *Quantas letras tem (sem considero espaços)
    *Quantas letras tem o primeiro nome"""

nome = input('Digite seu nome completo: ').strip()#ja foi cortado os espaços antes e depois da variavel

print('SEU NOME: {}.'.format(nome.upper()))
print('seu nome: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))#aqui leu o tamanho do nome e diminuiu os espaços em branco
primeironome = nome.split()
print('Seu nome tem {} letras.'.format(len(primeironome[0])))
#Outra resolução para qnt de letras do primeiro nome
    #print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))