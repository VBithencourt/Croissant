
import pygame
from mapa_F1 import mapa_1
from tela_inicial import mostrar_tela_inicial
from tela_tutorial import mostrar_tutorial
from player import *
from player2 import *
from tela_final_ import *

con = pygame.image.load('Coisinhas/pedragrama.jpg').convert()
Va1 = pygame.image.load('Coisinhas/cid.jpg').convert()
grama = pygame.image.load('Coisinhas/grama.png').convert()
P_lisa = pygame.image.load('Coisinhas/Fundoazul.jpg').convert()
P1 = pygame.image.load('Coisinhas/p1.png').convert()
P2 = pygame.image.load('Coisinhas/p2.png').convert()
P3 = pygame.image.load('Coisinhas/p5.png').convert()
P4 = pygame.image.load('Coisinhas/p4.png').convert()

pygame.mixer.music.load('musica/soundtrack.mpeg')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

efeito_sonoro = pygame.mixer.Sound('musica/botão.mpeg')
efeito_sonoro.set_volume(0.4) 
def tocar_efeito_sonoro():
    efeito_sonoro.play()
    pygame.time.set_timer(pygame.USEREVENT, 1500)



mostrar_tela_inicial(janela)

tutorial_ativo = False
jogo = True
som_tocado = False
game_over = False
tela_final = False

mortes_player = 0


player_chegou_no_4 = False


font_score = pygame.font.Font(None, 36)

font_score = pygame.font.Font(None, 36)
x_inicial = 20
y_inicial = 700
player = Player(x_inicial, y_inicial, 20, 20)

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
                
                game_over = False
                som_tocado = False  # Reinicia o som
                player_chegou_no_4 = False  # Reinicia o status de chegada
                
                tocar_efeito_sonoro()  # Toca o som novamente

        if event.type == pygame.USEREVENT:
            efeito_sonoro.stop()

    if game_over:
        # Se o jogo acabou, mostra a tela de Game Over
        font = pygame.font.Font(None, 74)
        texto = font.render("GAME OVER", True, (255, 0, 0))
        janela.blit(texto, (500, 300))

        texto_mortes_player = font_score.render(f'Mortes Player 1: {mortes_player}', True, (0, 0, 0))
        
        janela.blit(texto_mortes_player, (500, 480))
        

        font_button = pygame.font.Font(None, 36)
        button = font_button.render("Pressione R para Reiniciar", True, (0, 0, 0))
        janela.blit(button, (500, 400))
    elif tela_final:
        # Mostra a tela final e espera o jogador pressionar "Esc" para sair
        if mostrar_final(janela):
            jogo = False  # Encerra o jogo se "Esc" for pressionado

        texto_mortes_player = font_score.render(f'Mortes Player 1: {mortes_player}', True, (0, 0, 0))
       
        janela.blit(texto_mortes_player, (500, 400))
        


        # Botão para reiniciar
        font_button = pygame.font.Font(None, 36)
        button = font_button.render("Pressione R para Reiniciar", True, (0, 0, 0))
        janela.blit(button, (500, 500))
    else:
        # Jogo em andamento
        player.handle_input()
        player.fisica()


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
                    elif mapa_1[linha][coluna] == 3:
                        janela.blit(Va1, (x, y))
                    elif mapa_1[linha][coluna] == 'p1':
                        janela.blit(P1, (x, y))
                    elif mapa_1[linha][coluna] == 'p2':
                        janela.blit(P2, (x, y))
                    elif mapa_1[linha][coluna] == 'p3':
                        janela.blit(P3, (x, y))
                    elif mapa_1[linha][coluna] == 'p4':
                        janela.blit(P4, (x, y))

            player.draw(janela)
      

            # Verifica se algum jogador pisou no tile "3"
            player_pos = (player.rect.x // largura_tile, player.rect.y // altura_tile)


            if mapa_1[player_pos[1]][player_pos[0]] == 3:
                game_over = True  # Acabou o jogo, o player pisou no tile 3
                mortes_player += 1  # Incrementa a morte do player


            if mapa_1[player_pos[1]][player_pos[0]] == 3: #or mapa_1[player2_pos[1]][player2_pos[0]] == 3:
                game_over = True  # Acabou o jogo, um dos jogadores pisou no tile 3

            if mapa_2[player_pos[1]][player_pos[0]] == 3:
                    game_over = True  # Acabou o jogo, o player pisou no tile 3
                    mortes_player += 1  # Incrementa a morte do player

            if mapa_2[player_pos[1]][player_pos[0]] == 3: #mapa_2[player2_pos[1]][player2_pos[0]] == 3:
                    game_over = True  # Acabou o jogo, um dos jogadores pisou no tile 3
            
            
            if mapa_1[player_pos[1]][player_pos[0]] == 'p1' :# and mapa_3[player2_pos[1]][player2_pos[0]] == 'p1':
                    tela_final = True  # Vai para a tela final do jogo
            

            

             

    pygame.display.update()

pygame.quit()
