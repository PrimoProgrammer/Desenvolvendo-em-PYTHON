from pydoc import stripid

print('Desafio 022 - Manipulando texto')

'''Crie um programa que leia o nome completo de uma pessoa e mostre:')
    '- O nome com todas as letras maiúsculas.'
    '- O nome com todas minúsculas.
    '- Quantas letras ao todo(sem considerar espaços).
    '- Quantas letras tem o primeiro nome.'''

#nome = str(input('Digite seu nome: '))
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
'''print ('Utilizado .UPPER -> ', nome.upper())
print('Utilizado .LOWER -> ', nome.lower())
print('Utilizado .STRIP ->', nome.strip())
print ('Utilizado .SPLIT -> ',nome.split())
print('Utilizado .JOIN -> ','-'.join(nome))
print('Utilizado .LEN -> ',len(nome))
print('Utilizado .in ->', 'Guedes' in nome)
print('Quantas letra primeiro nome? ', len (nome.find()))'''

print('Seu nome em Maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minusculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separanome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separanome[0], len(separanome[0])))




