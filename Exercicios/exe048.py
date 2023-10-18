#Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de três e que se encontram no intervalo de 1 a 500

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 501, 2):#repita o contador do intervalo(inicio = 1, fim = 501, passo 2 em 2)
    if c % 3 == 0:# se contador for divisivel por 3
        soma = soma + c # acresente na variavel (acumuladora) o valor dela mais o valor encontrado no contador
        cont = cont + 1 #armazene na variavel cont qntos numeros e divisivel por 3
print(soma, cont)

