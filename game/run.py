import os
import pygame

dir_path = os.path.dirname(os.path.realpath(__file__))

pygame.init()
screen = pygame.display.set_mode((900, 700))

finished = False

x = 450 - 30 / 2  # middle of the screen taking playerImage into consideration
y = 650

playerImage = pygame.image.load("%s/images/playerImage.png" % dir_path)
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerImage = playerImage.convert_alpha()

backGroundImage = pygame.image.load("%s/images/background.png" % dir_path)
backGroundImage = pygame.transform.scale(backGroundImage, (900, 700))
screen.blit(backGroundImage, (0, 0))

treasureImage = pygame.image.load("%s/images/treasure.png" % dir_path)
treasureImage = pygame.transform.scale(treasureImage, (30, 30))
treasureImage = treasureImage.convert_alpha()

enemyImage = pygame.image.load("%s/images/enemy.png" % dir_path)
enemyImage = pygame.transform.scale(enemyImage, (30, 30))
enemyImage = enemyImage.convert_alpha()

treasureX = 450 - 30 / 2
treasureY = 50

enemyX = 110
enemyY = 580

screen.blit(treasureImage, (treasureX, treasureY))

frame = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 85)
level = 1
lives = 1

movingRight = True


def check_collision(x, y, treasureX, treasureY):
    global screen, text
    collisionState = False
    if y >= treasureY and y <= treasureY + 30:
        # the current y position is between tresureY and the height of the treasure
        if x >= treasureX and x <= treasureX + 30:
            # the x position is between tresureX and the width of the treasure
            y = 650
            collisionState = True
        elif x + 30 >= treasureX and x + 30 <= treasureX + 30:
            y = 650
            collisionState = True
    elif y + 30 >= treasureY and y + 30 <= treasureY + 30:
        if x >= treasureX and x <= treasureX + 30:
            y = 650
            collisionState = True
        elif x + 30 >= treasureX and x + 30 <= treasureX + 30:
            y = 650
            collisionState = True
    return collisionState, y


enemies = [(enemyX, enemyY, movingRight)]


while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    if lives == 0:
        pygame.display.flip()
        text = font.render("GAME OVER!!", True, (0, 0, 0, 0))
        screen.blit(text, (450 - text.get_width() / 2, 300))
        pygame.display.flip()
    else:
        pressedKeys = pygame.key.get_pressed()

        enemyIndex = 0
        for enemyX, enemyY, movingRight in enemies:
            if enemyX >= 810 - 30:
                movingRight = False
            elif enemyX <= 120:
                movingRight = True

            if movingRight:
                enemyX += 5 * level
            else:
                enemyX -= 5 * level

            enemies[enemyIndex] = (enemyX, enemyY, movingRight)
            enemyIndex += 1

        if pressedKeys[pygame.K_UP]:
            y -= 5
        if pressedKeys[pygame.K_DOWN]:
            y += 5
        if pressedKeys[pygame.K_LEFT]:
            x -= 5
        if pressedKeys[pygame.K_RIGHT]:
            x += 5

        # load images
        screen.blit(backGroundImage, (0, 0))
        screen.blit(treasureImage, (treasureX, treasureY))
        screen.blit(playerImage, (x, y))

        for enemyX, enemyY, movingRight in enemies:
            screen.blit(enemyImage, (enemyX, enemyY))
            collisionWithEnemy, y = check_collision(x, y, enemyX, enemyY)
            if collisionWithEnemy:
                text = font.render("You've lost a life", True, (0, 0, 0, 0))
                screen.blit(text, (450 - text.get_width() / 2, 300))
                pygame.display.flip()
                frame.tick(1)
                lives -= 1
            elif collisionWithEnemy and lives == 1:
                lives -= 1
                text = font.render("GAME OVER!!", True, (0, 0, 0, 0))
                screen.blit(text, (450 - text.get_width() / 2, 300))
                pygame.display.flip()

        # check for collision
        collisionWithTreasure, y = check_collision(x, y, treasureX, treasureY)
        if collisionWithTreasure:
            text = font.render("Level %s Complete!" % level, True, (0, 0, 0, 0))
            screen.blit(text, (450 - text.get_width() / 2, 300))
            pygame.display.flip()
            frame.tick(1)
            level += 1
            enemies.append((enemyX - 50 * level, enemyY - 50 * level, movingRight))

    pygame.display.flip()

    # change/sleep framerate
    frame.tick(30)
