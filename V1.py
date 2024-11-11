import pygame

#posicionamento cartesiano é sempre para baixa. ou seja, x aumenta pra direita e o y aumenta para baixo.

pygame.init()

janela = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Insper challengers: Em busca do croissant de chocolate.')

jogo = True

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    janela.fill((255, 255, 255))

    pygame.display.update()

pygame.quit()



