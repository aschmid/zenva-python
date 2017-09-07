import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    rectOne = pygame.Rect(0, 50, 30, 30)
    color   = (0, 0, 255)

    pygame.draw.rect(screen, color, rectOne)
    pygame.display.flip()
