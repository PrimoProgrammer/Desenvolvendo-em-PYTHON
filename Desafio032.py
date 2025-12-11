print('Desafio 032 - Condições')
print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')

from datetime import date
from time import sleep
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
print('Analisando....')
sleep(3)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
