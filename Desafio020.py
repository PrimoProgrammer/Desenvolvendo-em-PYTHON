print('==== Desafio 20 de Módulos ====')
print('O mesmo professor do desafio anterior, quer sortear a ordem de apresentação de tabalhos dos alunos. Faça um '
      'programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')

#import random ou
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)

'''MÉTODO RANDOM SHUFFLE EMBARALHA PARA ORDEM DE APRESENTAÇÃO'''
