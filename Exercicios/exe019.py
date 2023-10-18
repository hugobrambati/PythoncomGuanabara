#Um professor quer sortear um dos seus alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome deles a escrevendo o nome do escolhido

from random import choice
a1 = input('Digite o primeiro do Aluno: ')
a2 = input('Digite o segundo do Aluno: ')
a3 = input('Digite o terceiro do Aluno: ')
a4 = input('Digite o quarto do Aluno: ')

lista = [a1, a2, a3, a4] #criar uma lista dos participantes

sortear = choice(lista)

print('O sorteado(a) foi {}.'.format(sortear))

