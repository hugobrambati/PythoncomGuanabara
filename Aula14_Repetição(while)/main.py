""" for (repita), estrutura de repetição com variavel de controle
    While (enquanto), estrutura de repetição com teste lógico.

O WHILE É USADO QUANDO NÃO SE SABE QUANTAS REPETIÇÕES SERÁ NECESSARIO NO PROGRAMA    
"""

# DIFERENÇAS COM FOR E WHILE(IMPRIMIR NUMERO DE 1 ATE 10)

"""for n in range(1, 11):
    print(n)
print('ACABOU!')

n = 1
while n < 11:
    print(n)
    n = n + 1
print('ACABOU!')   

# qndo não sabemos a qntidade de vezes para executar o programas, precisamos usar uma flag(condição de parada)
n = 1
while n != 0: # enquanto n for diferente de 0, usamos o 0 como flag
    n = int(input("Digite um numero: "))# vai ficar pediddo numero
print('FIM!') """   

#Outro exemplo com flag

r = 'S'
n = 1 #iniciador de n
while r == 'S': #enquanto r for igual a S continue o programa
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N]')).upper
print('FIM!')