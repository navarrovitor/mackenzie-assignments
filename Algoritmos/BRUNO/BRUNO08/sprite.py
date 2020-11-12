import pygame

pygame.init()

larg, alt = 800, 500
cor_fundo = (255, 255, 255)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Demo Sprite")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()