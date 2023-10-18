#Faça um program aque leia a largura e a altura de uma parede em metros, calcule a sua area e a qnt de tinta necessaria para pintala, sabendo que cada litro de tinta pinta uma area de 2m2

lg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = lg * alt
tnt = area / 2

print('Sua parede tem a dimensão de {} x {} e sua area e de {}m²'.format(lg, alt, area))
print('Para pintar essa parede você vai precisar de {} litros de tinta'.format(tnt))
