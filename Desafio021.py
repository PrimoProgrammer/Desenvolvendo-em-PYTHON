print('==== Desafio 21 de Módulos ====')
print('Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.')

import pygame
pygame.init()
pygame.mixer.music.load('alok021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

'''A música foi copiada para a pasta junto com o arquivo do código, ao executar o código a musica se iniciará'''
