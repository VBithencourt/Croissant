import pygame
pygame.font.init()
fonte_personalizada = pygame.font.Font("Coisinhas/Fonte2.ttf", 190)
imagem_fundo = pygame.image.load("Coisinhas/Fundo2.jpeg")

def mostrar_tela_inicial(janela):
    iniciar = False
    while not iniciar:
        janela.blit(imagem_fundo, (0, 0))
        texto = "Pressione qualquer tecla para iniciar"
        texto_preto = fonte_personalizada.render(texto, True, (0, 0, 0))  # Texto preto
        texto_branco = fonte_personalizada.render(texto, True, (255, 255, 255))  # Texto branco (borda)
        texto_rect = texto_preto.get_rect(center=(1400 // 2, 800 // 2 + 330))
        janela.blit(texto_branco, (texto_rect.x - 2, texto_rect.y))  # Esquerda
        janela.blit(texto_branco, (texto_rect.x + 2, texto_rect.y))  # Direita
        janela.blit(texto_branco, (texto_rect.x, texto_rect.y - 2))  # Cima
        janela.blit(texto_branco, (texto_rect.x, texto_rect.y + 2))  # Baixo
        janela.blit(texto_branco, (texto_rect.x - 2, texto_rect.y - 2))  # Canto superior esquerdo
        janela.blit(texto_branco, (texto_rect.x + 2, texto_rect.y - 2))  # Canto superior direito
        janela.blit(texto_branco, (texto_rect.x - 2, texto_rect.y + 2))  # Canto inferior esquerdo
        janela.blit(texto_branco, (texto_rect.x + 2, texto_rect.y + 2))  # Canto inferior direito

        janela.blit(texto_preto, texto_rect)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                iniciar = True



       

        
