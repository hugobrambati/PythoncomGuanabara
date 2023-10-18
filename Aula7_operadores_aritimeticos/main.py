n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pnt = n1 ** n2
div_int = n1 // n2
rest_div = n1 % n2

print('Você digitou os numeros {} e {},\n a soma deles é {},\n a subtração entre eles é {},\n a multiplicação é {},\n a divisão é {:.3f},\n a pontencia é {},\n a divisão inteira é {},\n e o resto da divisão é {}'.format(n1, n2, soma, sub, mult, div, pnt, div_int, rest_div, end="******"))

