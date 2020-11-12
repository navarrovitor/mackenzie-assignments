import pygame

pygame.init()

sWidth = 500
sHeight = 480

win = pygame.display.set_mode((sWidth, sHeight))

pygame.display.set_caption("Hello World")

walkLeft = [
    pygame.image.load("Game/L1.png"),
    pygame.image.load("Game/L2.png"),
    pygame.image.load("Game/L3.png"),
    pygame.image.load("Game/L4.png"),
    pygame.image.load("Game/L5.png"),
    pygame.image.load("Game/L6.png"),
    pygame.image.load("Game/L7.png"),
    pygame.image.load("Game/L8.png"),
    pygame.image.load("Game/L9.png"),
]
walkRight = [
    pygame.image.load("Game/R1.png"),
    pygame.image.load("Game/R2.png"),
    pygame.image.load("Game/R3.png"),
    pygame.image.load("Game/R4.png"),
    pygame.image.load("Game/R5.png"),
    pygame.image.load("Game/R6.png"),
    pygame.image.load("Game/R7.png"),
    pygame.image.load("Game/R8.png"),
    pygame.image.load("Game/R9.png"),
]
bg = pygame.image.load("Game/bg.jpg")
char = pygame.image.load("Game/standing.png")

clock = pygame.time.Clock()


class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    hero.draw(win)
    pygame.display.update()


hero = player(0, 410, 64, 64)
run = True
# loop principal
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.right = False
        hero.left = True
        hero.standing = False
    elif keys[pygame.K_RIGHT] and hero.x + hero.width < sWidth - hero.vel:
        hero.x += hero.vel
        hero.right = True
        hero.left = False
        hero.standing = False
    else:
        hero.walkCount = 0
        hero.standing = True

    if not (hero.isJump):
        if keys[pygame.K_SPACE]:
            hero.isJump = True
            hero.right = False
            hero.left = False
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -10:
            neg = 1
            if hero.jumpCount < 0:
                neg = -1
            hero.y -= (hero.jumpCount ** 2) // 2 * neg
            # usando floor para evitar deprecation warning
            hero.jumpCount -= 1
            # velocidade do pulo
        else:
            hero.isJump = False
            hero.jumpCount = 10
    redrawGameWindow()
    # print(f'x = {x}, y = {y}')

pygame.quit()