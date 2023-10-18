#Faça um algoritimo que leia o salário e mostre seu novo salário com 15% de aumento

slr = float(input('Digite o salário: '))

amt = slr / 100 * 15

nvslr = slr + amt

print('O valor do salário atual é de R$:{}, aumento {:.4}, valor total novo R$:{}'.format(slr, amt, nvslr))