print('Desafio 028 - CONDIÇÕES')
print('Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça \n'
      'para o usuário tentar descobrir qual foi o número escolhido pelo computador.\n'
      'O programa deverá escrever na tela se o usuário venceu ou perdeu.')

from random import choice #modo sorteio
from time import sleep #modo aguardando
lista = [0, 1, 2, 3, 4, 5]
computador = choice(lista)
usuario = int(input('Adivinhe qual número o computador escolheu de 0 a 5? '))
print('O computador escolheu o número {}'.format(computador))
print('PROCESSANDO...')
sleep(5)
if computador == usuario:
    print('Parabéns você adivinhou número {} que o computador escolheu!'.format(computador))
else:
    print('Desculpe, mas você não acertou o número {}!'.format(computador))

#ouuuuuuuuuuuuuuuuuu
'''from random import randint
computador = randint(0 ,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))

if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei eu pensei no número {} e não no {}.'.format(computador, jogador))'''