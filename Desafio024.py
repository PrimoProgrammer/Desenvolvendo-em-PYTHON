print('Desafio 024 Manipulando texto')
print('Crie um programa que leia o nome de uma cidade, e diga se ela começa ou não com o nome "Santo"')

'''cidade = str(input('Digite nome de uma cidade: '))

print ('SANTO' in cidade)'''

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
