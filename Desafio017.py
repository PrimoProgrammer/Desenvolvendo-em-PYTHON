print('==== Desafio 17 de Módulos ====')
print('Faça um programa que leia o comprimento  do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa')

'''sem importação
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(h1)) '''

'''Com importação agora'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
