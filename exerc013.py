salário = float(input('Qual o salário do funcionário? R$'))
aumento = salário + (salário*15/100)
print(' O salário com aumento de 15% será R${:.2f}'.format(aumento))