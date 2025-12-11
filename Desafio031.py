print('Desafio 031 - Condições')
print('Desenvolva um programa que pergunte a distância de uma viagem em KM.\n'
      'Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens longas.\n\n')

'''d = float(input('Qual a distância da viagem em KM? '))
vcurtas = d * 0.50
vlongas = d * 0.45
if d <= 200:
    print('Você pagará na passagem R${:.2f} reais viajando a {}km de distância.'.format(vcurtas, d))
if d >= 201:
    print('Você pagará na passagem R${:.2f} reais viajando a {}km de distância.'.format(vlongas, d))'''

distancia = float(input('Qual a distância da sua viagem? '))
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
preço = distancia*0.50 if distancia <= 200 else distancia * 0.45 # modo simplificado
print('E o preço da sua passagem será R${:.2f}'.format(preço))