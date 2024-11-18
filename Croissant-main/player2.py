import pygame
from mapa_F1 import *

largura_tile = 20
altura_tile = 20

class Player2:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 0.8
        self.velocity_y = 0
        self.gravity = 0.2
        self.jump_strength = -10
        self.on_ground = False  # Inicialmente, o personagem não está no chão

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.movimentacao(-self.speed, 0)  # Movimenta para a esquerda
        if keys[pygame.K_d]:
            self.movimentacao(self.speed, 0)   # Movimenta para a direita
        if keys[pygame.K_w] and self.on_ground: # Pulo só se estiver no chão
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
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

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
player2 = Player2(x_inicial + 30, y_inicial, 20, 20)