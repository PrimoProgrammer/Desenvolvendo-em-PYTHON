print('Desafio 026 - Manipulando texto')
print('Faça um programa que leia uma frase pelo teclado e mostre: \n'
      'Quantas vezes aparece a letra "A".\n'
      'Em que posição ela aparece a primeira vez.\n'
      'Em que posição ela aparece a última vez.\n')

frase = str(input('Digite uma frase: ')).upper().strip()
print(frase, '\n')
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))


