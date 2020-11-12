import pygame, time

pygame.init()

l, a = 800, 500
cor_fundo = (0, 0, 0)
tela = pygame.display.set_mode((l, a))
pygame.display.set_caption("vitão e bia")

logo = pygame.image.load("image/logo_transparent.png")
logo = pygame.transform.scale(logo, (300, 300))
ret_logo = logo.get_rect()
vel_logo = [1, 1]

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill(cor_fundo)
    tela.blit(logo, ret_logo)
    ret_logo = ret_logo.move(vel_logo)
    if ret_logo.left < -15 or ret_logo.right > l + 15:
        vel_logo[0] = -vel_logo[0]
    if ret_logo.top < -50 or ret_logo.bottom > a + 50:
        vel_logo[1] = -vel_logo[1]

    pygame.display.update()
    time.sleep(10 / 1000)

pygame.quit()