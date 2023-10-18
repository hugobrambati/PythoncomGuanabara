""" Crie um programa que leia uma frase pelo teclado e mostre 
    *qnts vezes aparece a letra "A"
    *Em que posição ela aparece a primeira vezes
    *em que posição ela aparece a ultima vez"""

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A apareceu {} vezes'.format(frase.count('a')))
print('A primeira posição que ela apareceu foi {}'.format(frase.lower().find('a') + 1))
print('A ultima posição que ela apareceu foi {}'.format(frase.lower().rfind('a') + 1))