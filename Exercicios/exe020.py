#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada

from random import shuffle
a1 = input('Digite o primeiro do Aluno: ')
a2 = input('Digite o segundo do Aluno: ')
a3 = input('Digite o terceiro do Aluno: ')
a4 = input('Digite o quarto do Aluno: ')

lista = [a1, a2, a3, a4]

shuffle(lista)#para essa funcionalidade não precisa criar variavel pq ele so vai embaralhar a lista existente

print('A lista de apresentação será {}'.format(lista))
