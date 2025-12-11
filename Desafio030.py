print('Desafio 030 - CONDIÇÕES'),
print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.')

num = int(input('Digite um número: '))

print('Número digitado foi {}'.format(num))
if num % 2 == 0:
    print('Número digitado então é PAR!')
else:
    print('Número digitado é IMPAR!')

