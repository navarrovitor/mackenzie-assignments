import pygame
import os

# tela
pygame.init()
larg, alt = 800, 500
win = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Jogo Da Forca")

# imagens
imagens = []

for i in range(7):
    imagem = pygame.image.load(f"img/forca{str(i)}.png")
    imagens.append(imagem)

# botões
raio = 20
espaço_entre_botões = 15
letras = []
x_inicial = round((larg - (raio * 2 + espaço_entre_botões) * 13) / 2)
y_inicial = 400
letra_do_botão = 65
fonte_letra = pygame.font.SysFont("montserrat", 40)
for i in range(26):
    x = (
        x_inicial
        + espaço_entre_botões * 2
        + ((raio * 2 + espaço_entre_botões) * (i % 13))
    )  # i%13 serve para termos dois andares de botões
    y = y_inicial + ((i // 13) * (espaço_entre_botões + raio * 2))
    letras.append([x, y, chr(letra_do_botão + i)])

# variáveis
estado_boneco = 0
branco = (255, 255, 255)
cor_botão = (173, 0, 209)

# loop
fps = 60
running = True
clock = pygame.time.Clock()


def desenhar():
    win.fill(branco)

    # desenhar letras
    for i in letras:
        x, y, letra = i
        pygame.draw.circle(win, cor_botão, (x, y), raio, 2)
        texto = fonte_letra.render(letra, 1, cor_botão)
        win.blit(texto, (x - texto.get_width() // 2, y - texto.get_width() // 2))
    # desenhar boneco
    win.blit(imagens[estado_boneco], (150, 100))

    pygame.display.update()


while running:
    # clock.tick(fps)

    desenhar()

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit()