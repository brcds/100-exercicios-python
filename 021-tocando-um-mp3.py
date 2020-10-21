# Faça um programa python que abra e reproduza um áudio de um arquivo MP3;

import pygame

pygame.init()
pygame.mixer.music.load('seu mp3')
pygame.mixer.music.play()
pygame.event.wait()



