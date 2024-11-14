import pygame
pygame.font.init()
imagem_fundo = pygame.image.load("Coisinhas/Fundo.jpeg")

def mostrar_tutorial(janela):
    janela.blit(imagem_fundo, (0, 0))
    
    texto_tutorial = [
        "Tutorial do Jogo:",
        "1. Use as setas para mover.",
        "2. Pressione 'Espaço' para pular.",
        "3. Evite os obstáculos.",
        "4. O objetivo é chegar ao final do mapa e",
        "subir o elevador para a próxima fase.",
        "",
        "Pressione 'T' para voltar ao jogo."
    ]
    
    fonte_personalizada = pygame.font.Font("Coisinhas/Fontejogo.ttf", 170)

    y_offset = 170
    
    for linha in texto_tutorial:
        texto_renderizado = fonte_personalizada.render(linha, True, (255, 255, 255))  # Texto branco
        texto_renderizado2 = fonte_personalizada.render(linha, True, (0, 0, 0)) # Texto preto
        texto_rect = texto_renderizado.get_rect(center=(1400 // 2, y_offset))  # Centraliza na tela
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y))  # Esquerda
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y))  # Direita
        janela.blit(texto_renderizado2, (texto_rect.x, texto_rect.y - 2))  # Cima
        janela.blit(texto_renderizado2, (texto_rect.x, texto_rect.y + 2))  # Baixo
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y - 2))  # Canto superior esquerdo
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y - 2))  # Canto superior direito
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y + 2))  # Canto inferior esquerdo
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y + 2))  # Canto inferior direito
        janela.blit(texto_renderizado, texto_rect)
        y_offset += 100  # Aumenta o deslocamento para a próxima linha
    
    pygame.display.update()
