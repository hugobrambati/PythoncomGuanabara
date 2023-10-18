frase = 'curso em Video Python'

#Fatiamento
print(frase[9])#retorna o "V"
print(frase[9:13])#retorna 'Cur" inclui o 9 caracter e exclui o 13
print(frase[9:21:2])#retorna "vdopto" começou no 9 ate o 20 pulando de 2 em 2
print(frase[:5])#qndo não informado de onde vai começar ele começa do 0, o retorno seria 'Curso"
print(frase[::5])# não informou o inicio não informou o fim, vai pular de 5 em 5 a strig toda 
print(frase[15:])##qundo não indica onde termina ele começa por onde a indicação está e vai ate o final
print(frase[9::3])#indica o inicio, como não incida o final vai até o fim e pulando de 3 em 3

#Analise

print(len(frase))# Mostra o comprimento da string
print(frase.count('o'))#pede para mostrar qnts veses a letra 'o' aparece na frase
print(frase.count('o', 0, 13))#faz a analise e fatiamento junto, fatia do 0 ate o 12 e ve qntos 'o' tem 
print(frase.find('deo'))#vai retornar em que posição começou o que foi pedido
print(frase.find('Android'))# vai retornar -1 indicando que essa string não existe
print('Curso' in frase)# uso do operador in para saber se aquela strig faz parte da variavel, retorna true ou false

#Transformação

print(frase.replace('Python', 'Android'))#replace troca uma coisa por outra, para alterar a variavel que que colocar variavel = variavel.replace(o que quer trocar , para que vai trocar ) 
print(frase.upper())#O que for maiscula ele mantem o que for minuscula ele troca
print(frase.lower())#O que for minuscula ele mantem o que for maiuscula ele troca
print(frase.capitalize())# transforma a string toda em minusculo e a primeira letra em maiscula
print(frase.title())# transforma a primeira letra das palavras separadas por espaço em letra maiuscula
print(frase.upper().count('o'))#unindo funcionalidade


frase2 = '   Aprenda Python  '
print(frase2)
print(len(frase2))
print(frase2.strip())# retira os espaços em branco dao inicio e do fim da string
print(frase2.rstrip())# o r indica que vai retirar o espaço em branco do lado direito da string
print(frase2.lstrip())# o l indica que vai retirar o espaço em branco do lado esquerdo da string

#Divisão

dividido = frase.split()#criar um objeto que recebe uma lista de palavra da frase
print(dividido)
print(dividido[0])#mostra a posição do primeiro item da lista
print(dividido[0] [2])# O primeiro [] mostra a posição da lista o segundo [] mostra o que tem no index dessa lista

 

#Junção

frutas = ['banana', 'Maça', 'Pera']
print(frutas)
print(' '.join(frutas))# o join junta uma lista de string com o argumento que for passado dentro da aspas
