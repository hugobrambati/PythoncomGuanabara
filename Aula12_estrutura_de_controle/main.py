nome = str(input('Qual o seu nome? '))

#Condição Aninhada, uma estrutura de repetião dentro da outra.

if nome == 'Hugo':
    print('Que nome bonito!')
elif nome == 'Hugo Leonardo' or nome == 'Ana Paula':
    print('Que belo nome composto')
else:
    print('Que nome normal!')

print('Tenha um bom dia,  {}!'.format(nome))

