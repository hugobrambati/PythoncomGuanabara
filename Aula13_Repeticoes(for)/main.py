for c in range(0, 6):#vai printar 6x o OI
    print("0I")
print('Fim')"""

"""for c in range(1, 6):#vai printar 5x o c == contador, ignora o ultimo 
    print(c)
print('Fim')"""

"""for c in range(6, 0, -1):#vai printar de 6 ate 1, ignorando o 1 dentro dos parenteses (a primeira casa diz aonde vc quer ir , a segunda onde vc quer chegar, e a terceira como vai)
    print(c)
print('Fim')"""

"""for c in range(0, 7, 2):#vai printar de 0 ate 7 pulando de 2 em 2, ignorando o 7, dentro dos parenteses (a primeira casa diz aonde vc quer ir , a segunda onde vc quer chegar, e a terceira como vai)
    print(c)
print('Fim')"""

"""n = int(input('Digite um numero: '))
for c in range(0, n, +2):#vai printar de 0 ate o numero digitado pulando de 2 em 2
    print(c)
print('Fim')"""

"""inicio = int(input('Digite o Numero inicial: '))
fim = int(input('Digite o numero final: ')) 
passo = int(input('Em quantos passo: '))

for c in range(inicio, fim+1, passo):#vai printar o numero digitado inicial, ate o numero digitado final somando 1, pulando no numero de passos digitado 
    print(c)
print('Fim')"""

"""for c in range(0, 3):
    n = int(input("Digite um valor: "))# esse bloco diz que vai dar o input 3x
print("FIM")

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n#esse bloco diz que vai somar  n  na variavel  s com 4 digitos fornecido pelo usuario
print(s)

from time import sleep#funcionalidade de contagem de tempo

for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print('POW, POW, BUM')
