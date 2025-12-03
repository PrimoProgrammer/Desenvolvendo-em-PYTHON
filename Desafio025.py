print('Desafio 025 - Manipulando texto')
print('Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.')

nome = str(input('Qual é o seu nome Completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
