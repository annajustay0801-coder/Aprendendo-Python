A = float(input('Digite a altura da parede:'))
L = float(input('Digite a largura da parede:'))
a = A*L
print('A área da parede é {}m²'.format(a))
print('Para pintar essa parede você precisará de {:.2f}L de tinta'.format(a/2))