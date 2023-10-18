from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) 
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('-='* 20)
print('O computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[computador]))
print('-='* 20)
if computador == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Computador GANHOU')
    else:
        print('OPÇÂO INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('OPÇÂO INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÂO INVALIDA')
