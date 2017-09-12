import os
import pygame

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 0
y = 50

playerImage = pygame.image.load("%s/playerImage.jpg"%dir_path)
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerImage = playerImage.convert()

frame       = pygame.time.Clock()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_SPACE]:
        y += 5

    rectOne = pygame.Rect(x, y, 30, 30) # x,y,width,height

    # blue  = (0, 0, 255) # RGB
    # black = (0, 0, 0)
    white = (255, 255, 255)

    # fill the screen with black
    # before drawing a new recangle
    screen.fill(white)

    screen.blit(playerImage, (x, y))

    # pygame.draw.rect(screen, blue, rectOne)
    pygame.display.flip()

    frame.tick(30)
