import pygame
from mapa_F1 import mapa_1
from tela_inicial import mostrar_tela_inicial
from tela_tutorial import mostrar_tutorial
from musica import *
from player import *
from player2 import *

mostrar_tela_inicial(janela)

tutorial_ativo = False
jogo = True
som_tocado = False
game_over = False

mortes_player = 0
mortes_player2 = 0

font_score = pygame.font.Font(None, 36)

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:  # Ativa/Desativa o tutorial
                tutorial_ativo = not tutorial_ativo
                tocar_efeito_sonoro()
            if event.key == pygame.K_r and game_over:  # Reinicia o jogo
                # Restaura o mapa e a posição dos jogadores
                mapa_1 = [linha[:] for linha in mapa_1]  # Restaura o mapa
                player = Player(20, 700, 20, 20)  # Cria o player na posição inicial
                player2 = Player2(50, 700, 20, 20)  # Cria o player2 na posição inicial
                game_over = False
                som_tocado = False  # Reinicia o som
                tocar_efeito_sonoro()  # Toca o som novamente

        if event.type == pygame.USEREVENT:
            efeito_sonoro.stop()

    if game_over:
        # Se o jogo acabou, mostra a tela de Game Over
        font = pygame.font.Font(None, 74)
        texto = font.render("GAME OVER", True, (255, 0, 0))
        janela.blit(texto, (500, 300))

        texto_mortes_player = font_score.render(f'Mortes Player 1: {mortes_player}', True, (0, 0, 0))
        texto_mortes_player2 = font_score.render(f'Mortes Player 2: {mortes_player2}', True, (0, 0, 0))
        janela.blit(texto_mortes_player, (500, 400))
        janela.blit(texto_mortes_player2, (500, 440))


        # Botão para reiniciar
        font_button = pygame.font.Font(None, 36)
        button = font_button.render("Pressione R para Reiniciar", True, (0, 0, 0))
        janela.blit(button, (500, 500))
    else:
        # Jogo em andamento
        player.handle_input()
        player.fisica()
        player2.handle_input()
        player2.fisica()

        janela.fill((255, 255, 255))

        if tutorial_ativo:
            mostrar_tutorial(janela)
        else:
            if not som_tocado:
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

            player.draw(janela)
            player2.draw(janela)

            # Verifica se algum jogador pisou no tile "3"
            player_pos = (player.rect.x // largura_tile, player.rect.y // altura_tile)
            player2_pos = (player2.rect.x // largura_tile, player2.rect.y // altura_tile)

            if mapa_1[player_pos[1]][player_pos[0]] == 3:
                game_over = True  # Acabou o jogo, o player pisou no tile 3
                mortes_player += 1  # Incrementa a morte do player

            if mapa_1[player2_pos[1]][player2_pos[0]] == 3:
                game_over = True  # Acabou o jogo, o player2 pisou no tile 3
                mortes_player2 += 1  # Incrementa a morte do player2

            if mapa_1[player_pos[1]][player_pos[0]] == 3 or mapa_1[player2_pos[1]][player2_pos[0]] == 3:
                game_over = True  # Acabou o jogo, um dos jogadores pisou no tile 3
             

    pygame.display.update()

pygame.quit()
