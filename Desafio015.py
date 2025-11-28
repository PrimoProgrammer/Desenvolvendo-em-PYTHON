km = int(input('Quantos km rodado? '))
dias = int(input('Quantos dias alugados? '))
pago = (dias * 60.00) + (km * 0.15)
print('O valor total a ser pago é de {:.2f}'.format(pago))
