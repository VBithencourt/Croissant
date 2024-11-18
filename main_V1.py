import pygame
from mapa_F1 import mapa_1
from tela_inicial import mostrar_tela_inicial
from tela_tutorial import mostrar_tutorial
from musica import *

pygame.init()

janela = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Insper challengers: Em busca do croissant de chocolate.')

# Carregar imagens
con = pygame.image.load('Coisinhas/concreto.png').convert()
Va1 = pygame.image.load('Coisinhas/Vines-acid.png').convert()
grama = pygame.image.load('Coisinhas\grama.png').convert()
P_lisa = pygame.image.load('Coisinhas\ParedeLisa.png').convert()

largura_tile = 20
altura_tile = 20

personagem = pygame.Rect(100, 100, 20, 20)  #
velocidade = 0.7

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 0.8
        self.velocity_y = 0
        self.gravity = 0.2
        self.jump_strength = -10
        self.on_ground = False  # Inicialmente, o personagem não está no chão

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.movimentacao(-self.speed, 0)  # Movimenta para a esquerda
        if keys[pygame.K_RIGHT]:
            self.movimentacao(self.speed, 0)   # Movimenta para a direita
        if keys[pygame.K_UP] and self.on_ground: # Pulo só se estiver no chão
            self.velocity_y = self.jump_strength
            self.on_ground = False

    def movimentacao(self, dx, dy):
        # Movimentação horizontal
        self.rect.x += dx
        if self.checa_colisao():
            self.rect.x -= dx  # Reverte o movimento se houver colisão

        # Movimentação vertical
        self.rect.y += dy
        if self.checa_colisao():
            self.rect.y -= dy  # Reverte o movimento se houver colisão
            if dy > 0:  # Se o personagem estava caindo
                self.on_ground = True
                self.velocity_y = 0
            elif dy < 0:  # Se o personagem estava subindo
                self.velocity_y = 0

    def fisica(self):
        if not self.on_ground:  # Aplica gravidade somente se não estiver no chão
            self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Verificando colisão com o chão
        if self.checa_colisao():
            self.rect.y -= self.velocity_y  # Reverte o movimento vertical
            self.velocity_y = 0
            self.on_ground = True  # O personagem está tocando o chão
        else:
            self.on_ground = False  # O personagem não está tocando o chão

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def checa_colisao(self):
        # Verificando colisões com os blocos sólidos no mapa
        for linha in range(len(mapa_1)):
            for coluna in range(len(mapa_1[linha])):
                if mapa_1[linha][coluna] == 1:  # Blocos sólidos (terreno)
                    bloco = pygame.Rect(coluna * largura_tile, linha * altura_tile, largura_tile, altura_tile)
                    if self.rect.colliderect(bloco):
                        return True
        return False


x_inicial = (len(mapa_1[0]) * largura_tile) // 2
y_inicial = (len(mapa_1) * altura_tile) // 2
player = Player(x_inicial, y_inicial, 20, 20)

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
                elif mapa_1[linha][coluna] == 2:
                    janela.blit(grama, (x, y))

        player.draw(janela)

    pygame.display.update()

pygame.quit()
