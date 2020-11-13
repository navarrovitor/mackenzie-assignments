import pygame

pygame.init()

larg, alt = 800, 200
cor_fundo = (0, 0, 0)

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Demonstração Sprite")
tela.fill(cor_fundo)

walkLeft = [
    pygame.image.load("images/L1.png"),
    pygame.image.load("images/L2.png"),
    pygame.image.load("images/L3.png"),
    pygame.image.load("images/L4.png"),
    pygame.image.load("images/L5.png"),
    pygame.image.load("images/L6.png"),
    pygame.image.load("images/L7.png"),
    pygame.image.load("images/L8.png"),
    pygame.image.load("images/L9.png"),
]
walkRight = [
    pygame.image.load("images/R1.png"),
    pygame.image.load("images/R2.png"),
    pygame.image.load("images/R3.png"),
    pygame.image.load("images/R4.png"),
    pygame.image.load("images/R5.png"),
    pygame.image.load("images/R6.png"),
    pygame.image.load("images/R7.png"),
    pygame.image.load("images/R8.png"),
    pygame.image.load("images/R9.png"),
]

run = True
x = 100
y = 100
while run:
    tela.blit(walkRight[1], (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = 0
                while i < 9:
                    tela.blit(walkLeft[i], (x, y))
                    pygame.time.delay(50)
                    pygame.display.update()
                    tela.fill(cor_fundo)
                    i += 1
                    x -= 2
            if event.key == pygame.K_RIGHT:
                for i in range(len(walkRight)):
                    mov = walkRight[i].get_rect()
                    tela.blit(walkRight[i], (x, y))
                    x += 2
                    pygame.time.delay(50)
                    pygame.display.update()
                    tela.fill(cor_fundo)
    pygame.display.update()
pygame.quit()