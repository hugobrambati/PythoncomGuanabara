#Faça um programa phyton que abra e reproduza o audio de um arquivo mp3
#copiar e colar o arquivo em mp3 para dentro do projeto.abs

import pygame

pygame.init()

pygame.mixer.music.load('exe21.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
