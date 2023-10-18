#Desenvolva um programa que leia 6 numeros inteiros e mostre apenas daqueles que forem pares.Se o valor digitado for impar desconsidere- o.abs
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(cont, soma)
        