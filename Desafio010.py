print('==== Desafio 10 - Real em dolar ====')

dinheiro = float(input('Digite quanto você tem em R$(reais) na carteira  para comprar em dollar? '))
dollarhoje = 5.34
conversaodolar = dinheiro / dollarhoje
print('Considerando o dolar USD {} dolares , com R$ {} Reais na carteira, '
      'conseguirá comprar {:.2f} dolares para viajar.'.format(dollarhoje, dinheiro, conversaodolar))