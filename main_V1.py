import pygame
from mapa_F1 import mapa_1
from tela_inicial import mostrar_tela_inicial
from tela_tutorial import mostrar_tutorial

pygame.init()
pygame.mixer.init()

janela = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Insper challengers: Em busca do croissant de chocolate.')

pygame.mixer.music.load('Coisinhas/soundtrack.mpeg') 
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) 

efeito_sonoro = pygame.mixer.Sound('Coisinhas/efeito_sonoro_botão.mpeg')
efeito_sonoro.set_volume(0.4) 

con = pygame.image.load('Coisinhas/concreto.png').convert()
Va1 = pygame.image.load('Coisinhas/Vines-acid.png').convert()
grama = pygame.image.load('Coisinhas\grama.png').convert()
P_lisa = pygame.image.load('Coisinhas\ParedeLisa.png').convert()
largura_tile = 20
altura_tile = 20

def tocar_efeito_sonoro():
    efeito_sonoro.play()
    pygame.time.set_timer(pygame.USEREVENT, 1500)

mostrar_tela_inicial(janela)

tutorial_ativo = False
jogo = True
som_tocado = False


while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:  # Verifica se a tecla 'T' foi pressionada
                tutorial_ativo = not tutorial_ativo  # Alterna entre ativar e desativar o tutorial
                tocar_efeito_sonoro()
        if event.type == pygame.USEREVENT:
            efeito_sonoro.stop()



    janela.fill((255, 255, 255))

    if tutorial_ativo:
        mostrar_tutorial(janela)
    else:
        if not som_tocado:  # Toca o som apenas uma vez ao entrar no mapa principal
            tocar_efeito_sonoro()
            som_tocado = True
        for linha in range(len(mapa_1)):
            for coluna in range(len(mapa_1[linha])):
                x = coluna * largura_tile
                y = linha * altura_tile
                if mapa_1[linha][coluna] == 1:
                    janela.blit(con, (x, y))
                elif mapa_1[linha][coluna] == 0:
                    janela.blit(P_lisa, (x, y))
                elif mapa_1[linha][coluna] == 2:
                    janela.blit(grama, (x, y))
                    
    pygame.display.update()

pygame.quit()


