import pygame
from mapa_F1 import mapa_1
#posicionamento cartesiano é sempre para baixa. ou seja, x aumenta pra direita e o y aumenta para baixo.

pygame.init()

janela = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Insper challengers: Em busca do croissant de chocolate.')

con = pygame.image.load('Coisinhas/concreto.png').convert()
Va1 = pygame.image.load('Coisinhas/Vines-acid.png').convert()
grama = pygame.image.load('Coisinhas\grama.png').convert()
P_lisa = pygame.image.load('Coisinhas\ParedeLisa.png').convert()
largura_tile = 20
altura_tile = 20


jogo = True

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    janela.fill((255, 255, 255))

# Desenha o mapa 1
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


