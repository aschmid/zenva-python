import os
import pygame

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 450-30/2 # middle of the screen taking playerImage into consideration
y = 650

playerImage = pygame.image.load("%s/images/playerImage.png"%dir_path)
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerImage = playerImage.convert_alpha()

backGroundImage = pygame.image.load("%s/images/background.png"%dir_path)
backGroundImage = pygame.transform.scale(backGroundImage,(900, 700))
screen.blit(backGroundImage, (0, 0))

treasureImage = pygame.image.load("%s/images/treasure.png"%dir_path)
treasureImage = pygame.transform.scale(treasureImage, (30, 30))
treasureImage = treasureImage.convert_alpha()

treasureX = 450-30/2
treasureY = 50

screen.blit(treasureImage, (treasureX, treasureY))

frame       = pygame.time.Clock()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[pygame.K_UP]:
        y -= 5
    if pressedKeys[pygame.K_DOWN]:
        y += 5
    if pressedKeys[pygame.K_LEFT]:
        x -= 5
    if pressedKeys[pygame.K_RIGHT]:
        x += 5

    # rectOne = pygame.Rect(x, y, 30, 30) # x,y,width,height

    # blue  = (0, 0, 255) # RGB
    # black = (0, 0, 0)
    # white = (255, 255, 255)

    # fill the screen with color
    # before drawing a new recangle
    # screen.fill(white)

    # load images
    screen.blit(backGroundImage, (0, 0))
    screen.blit(treasureImage, (treasureX, treasureY))
    screen.blit(playerImage, (x, y))

    # check for collision
    if y >= treasureY and y <= treasureY+30:
        if x >= treasureX and x <= treasureX+30:
            pass
        elif x+30 >= treasureX and x+30 <= treasureX+30:
            pass

    elif y+30 >= treasureY and y+30 <= treasureY+30:
        if x >= treasureX and x <= treasureX+30:
            pass
        elif x+30 >= treasureX and x+30 <= treasureX+30:
            pass




    # pygame.draw.rect(screen, blue, rectOne)
    pygame.display.flip()

    # change/sleep framerate
    frame.tick(30)
