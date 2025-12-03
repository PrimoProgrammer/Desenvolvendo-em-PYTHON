print('Desafio 027 -  Manipulando texto \n')
print('Faça um programa que leia o nome completo de uma pessoa.\n'
      'Mostrando em seguida o primeiro e o último nome separadamente.\n'
      'ex: Ana Maria de Souza, primeiro=Ana e último=Souza\n')

n = str(input('Digite seu nome completo: ')).strip() # retirando todos os espaços
nome = n.split() # separando as palavras
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0])) # primeiro nome
print('Seu último nome é {}.'.format(nome[len(nome)-1])) # -1 negativo se refere ao ultimo nome e -2 o penultimo nome.