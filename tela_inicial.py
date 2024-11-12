import pygame
pygame.font.init()
fonte_personalizada = pygame.font.Font("Coisinhas/Fonte.ttf", 74)

def mostrar_tela_inicial(janela):
    iniciar = False
    while not iniciar:
        janela.fill((0, 0, 0))  # Fundo preto
        texto = fonte_personalizada.render("Pressione qualquer tecla para iniciar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(1400 // 2, 800 // 2))
        janela.blit(texto, texto_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                iniciar = True