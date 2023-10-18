#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.

print('-=-' * 20)
print('Analisador de triangulos')
print('-=-' * 20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo')
else:
    print("Os seguimentos acima não podem formar um triangulo")