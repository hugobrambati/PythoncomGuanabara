#Crie um programa que o usuario digite o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.
    # EX: Ana Maria de Souza
    #Primeiro = Ana
    #Ultimo = Souza

nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()
print('Seu primeiro nome é {}'.format(lista_nome[0]))
print('Seu ultimo nome é {}'.format(lista_nome[len(lista_nome)- 1]))
