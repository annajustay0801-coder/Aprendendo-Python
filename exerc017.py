co = float(input('Digite o tamanho do cateto oposto:'))
ca = float(input('Digite o tamanho do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A medida da hipotenusa deste triângulo retângulo é {:.2f}'.format(hi))


import math
co = float(input('Digite a medida do cateto oposto:'))
ca = float(input('Digite a medida do cateto adjacente:'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))