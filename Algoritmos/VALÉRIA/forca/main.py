import pygame
import math
import random

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
fonte_palavra = pygame.font.SysFont("montserrat", 60)
for i in range(26):
    x = (
        x_inicial
        + espaço_entre_botões * 2
        + ((raio * 2 + espaço_entre_botões) * (i % 13))
    )  # i%13 serve para termos dois andares de botões
    y = y_inicial + ((i // 13) * (espaço_entre_botões + raio * 2))
    letras.append([x, y, chr(letra_do_botão + i), True])

# variáveis
estado_boneco = 0
branco = (255, 255, 255)
cor_botão = (173, 0, 209)
cor_palavra = (186, 86, 36)
palavras = open("palavras.txt").read().splitlines()
dicas = open("dicas.txt").read().splitlines()
palavra = random.choice(palavras)
dica = dicas[palavras.index(palavra)]
letras_adivinhadas = []

# loop
fps = 60
running = True
clock = pygame.time.Clock()


def desenhar():
    win.fill(branco)
    texto_dica = fonte_palavra.render(f"Dica: {dica}", 1, cor_palavra)
    win.blit(texto_dica, (150, 50))

    # desenhar palavra
    palavra_jogada = ""
    for i in palavra:
        if i in letras_adivinhadas:
            palavra_jogada += f"{i} "
        else:
            palavra_jogada += "_ "
    texto = fonte_palavra.render(palavra_jogada, 1, cor_palavra)
    win.blit(texto, (400, 200))

    # desenhar letras
    for i in letras:
        x, y, letra, botao_visivel = i
        if botao_visivel:
            pygame.draw.circle(win, cor_botão, (x, y), raio, 2)
            texto = fonte_letra.render(letra, 1, cor_botão)
            win.blit(texto, (x - texto.get_width() // 2, y - texto.get_width() // 2))
    # desenhar boneco
    win.blit(imagens[estado_boneco], (150, 100))

    pygame.display.update()


def fim_de_jogo(frase):
    pygame.time.delay(2000)
    win.fill(branco)
    texto = fonte_palavra.render(frase, 1, cor_palavra)
    win.blit(texto, (200, 250))
    pygame.display.update()
    pygame.time.delay(3000)


while running:
    # clock.tick(fps)

    desenhar()

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Colisões de botões
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in letras:
                x, y, letra, botao_visivel = i
                if botao_visivel:
                    distancia = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                    if distancia < raio:
                        letras_adivinhadas.append(letra)
                        i[3] = False
                        if letra not in palavra:
                            estado_boneco += 1
    ganhou = True
    for i in palavra:
        if i not in letras_adivinhadas:
            ganhou = False
            break

    if ganhou:
        fim_de_jogo("VOCE GANHOU!")
        break

    if estado_boneco == 6:
        fim_de_jogo("VOCE PERDEU")
        break

pygame.quit()