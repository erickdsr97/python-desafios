# esse programa calcula o preço a ser pago pelo aluguel de um carro, baseado nos dias alugados e nos km rodados
km = float(input('Quantidade de km(s) rodados: '))
dias = int(input('Quantidade de dias alugado: '))
dia = dias * 60
kms = float(km * 0.15)
total = float(dia + kms)
print('O valor pelo(s) dia(s) em que o carro foi alugado é de R${:.2f} e pelos kms rodados é de R${:.2f}'.format(dia, kms))
print('Os valores somados dão um total de R${:.2f}'.format(total))
# reforçar que para diminuir o tamanho da casa decimal ou diminui, simplesmente utiliza :. e logo após isso o número
# seguido de um f

