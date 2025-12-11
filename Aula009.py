from os.path import split
print('Aula009 Manipulanto texto com fatiamento, análise e transformação')
print('==== Manipulando texto ====')

'''Praticando todos códigos possíveis de manipulação do Curso em vídeo'''
frase = ('   Curso em vídeo Python')
print(frase[13:])
print(frase[:13])
print(frase[3])
print(frase[1:21:3])
print(frase[1::2])
print(frase[3:10])
print(frase.count('o')) # quantas letras minúsculas
print(frase.upper().count('O')) #Conta quantas letras 'ÓS' maíusculas tem na frase com UPPER
print(len(frase)) # Exibi comprimento do texto (quantos caracteres)
print(frase.strip()) # removendo os espaços desnecessários
frase = frase.replace('Python', 'Android') # substitui a palavra Python para Android
print(frase) # exibi a frase modificada para android
print(frase.strip()) #remove os espaços desnecessários
print('Curso' in frase) #está querendo saber se a palavra Curso está dentro da frase
print(frase.lower().find('vídeo')) #vai procurar na frase a palavra vídeo
print(frase.split())
dividido = frase.split() # vai fatiar as palavras da frase separando-as
print(dividido[2]) # vai exibir a palavra vídeo na posição 2
print(dividido[2][3]) # vai exibir apenas a letra e

'''Desafios para fazer: 
Desafio 22 em diante'''



