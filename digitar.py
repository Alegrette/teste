import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Digitar")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza_escuro = (80, 80, 80)
cinza_claro = (200, 200, 200)
azul = (0, 0, 255)

# Fontes
pygame.font.init()
fonte_titulo = pygame.font.SysFont("Arial", 48)
fonte_texto = pygame.font.SysFont("Arial", 36)
fonte_pontuacao = pygame.font.SysFont("Arial", 24)

# Frases
frases = ["Digite print(variavel)", "Digite pygame.init()", "Digite pygame.quit()", "Digite pygame.time.get_ticks()",
          "Digite pygame.display.set_caption()", "Digite pygame.font.SysFont()", "Digite random.choice()",
          "Digite pygame.event.get()", "Digite variavel.split()", "Digite variavel.fill()"]
frase_atual = random.choice(frases)
resposta_correta = frase_atual.split()[-1]

# Pontuação
pontuacao = 0

# Tempo
tempo_limite = 10
tempo_inicio = pygame.time.get_ticks()

# Loop principal do jogo
jogo_executando = True
resposta_usuario = ""

while jogo_executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_executando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if resposta_usuario.lower() == resposta_correta:
                    pontuacao += 1
                    tempo_inicio = pygame.time.get_ticks()
                frase_atual = random.choice(frases)
                resposta_correta = frase_atual.split()[-1]
                resposta_usuario = ""
            elif event.key == pygame.K_BACKSPACE:
                resposta_usuario = resposta_usuario[:-1]
            else:
                resposta_usuario += event.unicode

    tempo_decorrido = (pygame.time.get_ticks() - tempo_inicio) // 1000

    if tempo_decorrido >= tempo_limite:
        # Jogador perdeu o jogo, faça algo aqui (ex: encerrar o jogo, mostrar mensagem)
        jogo_executando = False

    janela.fill(branco)

    # Renderização do título
    titulo_renderizado = fonte_titulo.render("Complete a Frase", True, preto)
    titulo_rect = titulo_renderizado.get_rect(center=(largura // 2, 80))
    janela.blit(titulo_renderizado, titulo_rect)

    # Renderização da frase atual
    frase_renderizada = fonte_texto.render(frase_atual, True, preto)
    frase_rect = frase_renderizada.get_rect(midtop=(largura // 2, 180))
    janela.blit(frase_renderizada, frase_rect)

    # Renderização da resposta do jogador
    resposta_renderizada = fonte_texto.render(resposta_usuario, True, preto)
    resposta_rect = resposta_renderizada.get_rect(midtop=(largura // 2, 280))
    janela.blit(resposta_renderizada, resposta_rect)

    # Renderização da pontuação
    pontuacao_renderizada = fonte_pontuacao.render("Pontuação: " + str(pontuacao), True, preto)
    pontuacao_rect = pontuacao_renderizada.get_rect(topright=(largura - 20, 20))
    janela.blit(pontuacao_renderizada, pontuacao_rect)

    # Renderização do temporizador
    tempo_restante = max(tempo_limite - tempo_decorrido, 0)
    tempo_renderizado = fonte_pontuacao.render("Tempo: " + str(tempo_restante), True, preto)
    tempo_rect = tempo_renderizado.get_rect(topright=(largura - 20, 60))
    janela.blit(tempo_renderizado, tempo_rect)


    pygame.display.flip()

pygame.quit()
