import pygame
pygame.font.init()
imagem_fundodf = pygame.image.load("Coisinhas/Final_Croissant.jpeg")

def mostrar_final(janela):
    # Mostra a tela final
    janela.blit(imagem_fundodf, (0, 0))
    
    texto = [
        "PARABÉNS!",
        "Você subiu todo o P2 e",
        "conquistou seu croissant de chocolate.",
        "Pressione 'Esc' para encerrar sua jornada."
    ]
    
    fonte_personalizada = pygame.font.Font("Coisinhas/Fontejogo.ttf", 170)
    y_offset = 170
    
    # Renderiza o texto na tela
    for linha in texto:
        texto_renderizado = fonte_personalizada.render(linha, True, (255, 255, 255))  # Texto branco
        texto_renderizado2 = fonte_personalizada.render(linha, True, (0, 0, 0)) # Texto preto
        texto_rect = texto_renderizado.get_rect(center=(1400 // 2, y_offset))  # Centraliza na tela
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y))  # Sombra esquerda
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y))  # Sombra direita
        janela.blit(texto_renderizado2, (texto_rect.x, texto_rect.y - 2))  # Sombra cima
        janela.blit(texto_renderizado2, (texto_rect.x, texto_rect.y + 2))  # Sombra baixo
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y - 2))  # Canto superior esquerdo
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y - 2))  # Canto superior direito
        janela.blit(texto_renderizado2, (texto_rect.x - 2, texto_rect.y + 2))  # Canto inferior esquerdo
        janela.blit(texto_renderizado2, (texto_rect.x + 2, texto_rect.y + 2))  # Canto inferior direito
        janela.blit(texto_renderizado, texto_rect)
        y_offset += 100  # Aumenta o deslocamento para a próxima linha

    pygame.display.update()

    # Loop para esperar o usuário pressionar "Esc"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Sai do jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True  # Reinicia o jogo e volta para a tela inicial
