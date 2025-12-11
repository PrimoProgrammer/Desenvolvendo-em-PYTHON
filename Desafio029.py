print('Desafio 029 - Condições Radar Eletrônico')
print('Escreva um programa que leia a velocidade de um carro.\n'
      'Se ele ultapassar "80kmh", mostre uma mensagem dizendo que ele foi multado.\n'
      'A multa vai custar R$ 7, 00 por cada km acima do limite.\n')

'''vel = int(input('Digite a velocidade que você passou no radar? '))
multa = (vel - 80) * 7
if vel >= 81:
    print('MULTADO: Você ultapassou o limite de velocidade e terpa que pagar R$ {:.2f}'.format(multa))
else:
    print('Você não será multado, porque não ultapassou a velocidade da via!')'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) *7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')

