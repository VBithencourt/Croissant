import pygame
pygame.mixer.init()
pygame.mixer.music.load('Coisinhas/soundtrack.mpeg') 
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) 

efeito_sonoro = pygame.mixer.Sound('Coisinhas/efeito_sonoro_botão.mpeg')
efeito_sonoro.set_volume(0.4)

def tocar_efeito_sonoro():
    efeito_sonoro.play()
    pygame.time.set_timer(pygame.USEREVENT, 1500)

