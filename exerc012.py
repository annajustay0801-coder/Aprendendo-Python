preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço*5/100)
print('O valor do produto na promoção com desconto de 5% vai ser R${:.2f}'.format(novo))