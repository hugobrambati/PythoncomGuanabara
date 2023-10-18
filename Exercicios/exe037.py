#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher a base da convesão:
# 1 para binario
# 2 para octal
# 3 hexadecimal

n = int(input('Digite um numero: '))
opcao = str(input('Digite:\n1 para binário\n 2 para octal\n 3 para hexadecima '))

if opcao == '1':
    binario = bin(n)[2:]#fatiamento de string começando do 2 para frente
    print('O numero {} convertido para binario é {}'.format(n, binario))
elif opcao == '2':
    octal = oct(n)[2:]
    print('O numero {} convertido para octal é {}'.format(n, octal))
elif opcao == '3':
    hdec = hex(n)[2:]
    print('O numero {} convertido para hexadecimal é {}'.format(n, hdec))
else:
    print('Opcao invalida!')

