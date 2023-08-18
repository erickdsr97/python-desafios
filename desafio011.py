# programa que calcula a quantidade de tinta necessária para pintar a parede
larg = int(input('Qual é a largura da parede? '))
alt = int(input('Qual é a altura da parede? '))
area = int(larg * alt)
tint = int(area / 2)
print('Serão necessárias {} latas de tinta para realizar a pintura, visto que a área da parede é de {}m²'.format(tint, area))
# saiu melhor do que o esperado

