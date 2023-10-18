#import math -> importa toda biblioteca math

# from math import = ceil -> importa da biblioteca math somente a funcionalidade ceil

# from math import = ceil, sqrt -> importa da biblioteca math a funcionalidade ceil e sqrt

"""import math #importei a biblioteca math toda

num = int(input('Digite um numero: '))
raiz = math.sqrt(num) # a variavel raiz vai receber da biblioteca a função sqrt
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz)))

from math import sqrt #importei somente a funcionalidade sqrt

num = int(input('Digite um numero: '))
raiz = sqrt(num)# diferente de importar a biblioteca toda não preciso colocar .
print('A raiz de {} é igual a {:.2}'.format(num, raiz))

import random

#peça para o computador te dar um numero aleatorio

num0= random.random()#retorna um float de 0 ate 1
num1 = random.randint(1, 20)#retorna um numero inteiro de 1 ate 10
print('Randon: {}'.format(num0))
print('Randint: {}'.format(num1))"""

import emoji

print(emoji.emojize("Ola mundo 😎"))



