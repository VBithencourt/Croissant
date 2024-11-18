import pygame
from mapa_F1 import *

pygame.init()

janela = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Insper challengers: Em busca do croissant de chocolate.')

# Carregar imagens
con = pygame.image.load('Coisinhas/concreto.png').convert()
Va1 = pygame.image.load('Coisinhas/Vines-acid.png').convert()
grama = pygame.image.load('Coisinhas\grama.png').convert()
P_lisa = pygame.image.load('Coisinhas\ParedeLisa.png').convert()


largura_tile = 20
altura_tile = 20

class Player:
    def __init__(self, x, y, width, height):
        self.frames = [
            pygame.image.load('Coisinhas/sprite1.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite2.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite3.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite4.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite5.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite6.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite7.png').convert_alpha(),
            pygame.image.load('Coisinhas/sprite8.png').convert_alpha()
        ]

        self.image = self.frames[0]
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = 0.8
        self.velocity_y = 0
        self.gravity = 0.2
        self.jump_strength = -6.75
        self.on_ground = False  # Inicialmente, o personagem não está no chão

        
        self.frame_index = 0  # Índice do quadro atual
        self.frame_rate = 200  # Tempo entre as trocas de quadros em milissegundos
        self.last_update = pygame.time.get_ticks()  # Marca o tempo da última troca de quadro
        self.image = self.frames[self.frame_index]  # Começa com o primeiro quadro
        self.facing_right = True  # O personagem começa olhando para a direita



    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.movimentacao(-self.speed, 0)  # Movimenta para a esquerda
            self.facing_right = False  # O personagem está indo para a esquerda
        if keys[pygame.K_RIGHT]:
            self.movimentacao(self.speed, 0)   # Movimenta para a direita
            self.facing_right = True  # O personagem está indo para a direita
        if keys[pygame.K_UP] and self.on_ground: # Pulo só se estiver no chão
            self.velocity_y = self.jump_strength
            self.on_ground = False

    def movimentacao(self, dx, dy):
        # Movimentação horizontal
        self.rect.x += dx
        if self.checa_colisao3():
            self.rect.x -= dx  # Reverte o movimento se houver colisão

        # Movimentação vertical
        self.rect.y += dy
        if self.checa_colisao3():
            self.rect.y -= dy  # Reverte o movimento se houver colisão
            if dy > 0:  # Se o personagem estava caindo
                self.on_ground = True
                self.velocity_y = 0
            elif dy < 0:  # Se o personagem estava subindo
                self.velocity_y = 0
    def checa_colisao3(self):
        # Verificando colisões com os blocos sólidos no mapa
        for linha in range(len(mapa_3)):
            for coluna in range(len(mapa_3[linha])):
                if mapa_3[linha][coluna] == 1:  # Blocos sólidos (terreno)
                    bloco = pygame.Rect(coluna * largura_tile, linha * altura_tile, largura_tile, altura_tile)
                    if self.rect.colliderect(bloco):
                        return True
        return False
    

    def fisica3(self):
        if not self.on_ground:  # Aplica gravidade somente se não estiver no chão
            self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Verificando colisão com o chão
        if self.checa_colisao3():
            self.rect.y -= self.velocity_y  # Reverte o movimento vertical
            self.velocity_y = 0
            self.on_ground = True  # O personagem está tocando o chão
        else:
            self.on_ground = False  # O personagem não está tocando o chão

        self.update()
        # Verificando colisão com o chão

    def update(self):
        now = pygame.time.get_ticks()
        
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)  # Alterna entre os quadros
            self.image = self.frames[self.frame_index]  # Atualiza a imagem do personagem

            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)


    def draw(self, janela):
        janela.blit(self.image, (self.rect.x, self.rect.y - self.image.get_height() + self.rect.height))




    
