print('==== Desafio 11 Orçamento de material para realizar um serviço de pintura ====')

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
litrotinta = int (area/2)

print('Uma parede com a Largura de {} e altura de {}, possui {}m².'.format(largura, altura, area))
print('Para pintar uma area de {}m², será necessário comprar {} litros de tintas. \n'
      'Pois cada litro de tinta pinta 2m².'.format(area, litrotinta))