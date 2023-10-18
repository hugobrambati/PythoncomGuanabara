# Condições simples

"""tempo= int (input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('------FIM-----')

#Condição simplificada

print('Carro Novo' if tempo <=3 else 'Carro Velho"')
print('------FIM-----')

nome = str(input('Digite seu nome: ')).strip()

if nome == 'Gustavo':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome e tão normal! ')
print('Bom dia ! {}'. format(nome))"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >= 5:
    print('Parabens vc está aprovado! , sua media foi {}'.format(media))
else:
    print('Estude mais vc está reprovado!, sua media foi {}'.format(media))
print('------FIM------')