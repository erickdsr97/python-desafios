# algoritmo que irá ler um preço de um produto e mostrar o novo preço com 5% de desconto
atual = int(input('Digite o valor atual do produto: '))
desconto = atual * 0.05
novo = atual + desconto
print('O preço do seu produto era de {}, com o desconto de 5% no valor de {}, o preço do seu produto passa a ser {}!'.format(atual, desconto, novo))



