import math
import random
import pygame
from pygame import mixer
import mainGame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space_img/background.png')

# Sound
mixer.music.load("space_img/background.wav")
mixer.music.play(-1)

# Caption and Icon

pygame.display.set_caption("Corona Invaiders")
icon = pygame.image.load('img/virus.png')

pygame.display.set_icon(icon)

global mainGame
mainGame = mainGame.MainGame()



def show_score(x, y):
    score = mainGame.font.render("Score : " + str(mainGame.score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = mainGame.over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(mainGame.playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(mainGame.enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(mainGame.bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(mainGame.enemyX - mainGame.bulletX, 2) + (math.pow(mainGame.enemyY - mainGame.bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def gameLoop():
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mainGame.playerX_change = -5
            if event.key == pygame.K_RIGHT:
                mainGame.playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("space_img/laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    mainGame.bulletX = mainGame.playerX
                    fire_bullet(mainGame.bulletX, mainGame.bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mainGame.playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    mainGame.playerX += mainGame.playerX_change
    if mainGame.playerX <= 0:
        mainGame.playerX = 0
    elif mainGame.playerX >= 736:
        mainGame.playerX = 736

    # Enemy Movement
    for i in range(mainGame.num_of_enemies):

        # Game Over
        if mainGame.enemyY[i] > 440:
            for j in range(mainGame.num_of_enemies):
                mainGame.enemyY[j] = 2000
            game_over_text()
            break

        mainGame.enemyX[i] += mainGame.enemyX_change[i]
        if mainGame.enemyX[i] <= 0:
            mainGame.enemyX_change[i] = 4
            mainGame.enemyY[i] += mainGame.enemyY_change[i]
        elif mainGame.enemyX[i] >= 736:
            mainGame.enemyX_change[i] = -4
            mainGame.enemyY[i] += mainGame.enemyY_change[i]

        # Collision
        collision = isCollision(mainGame.enemyX[i], mainGame.enemyY[i], mainGame.bulletX, mainGame.bulletY)
        if collision:
            explosionSound = mixer.Sound("space_img/explosion.wav")
            explosionSound.play()
            mainGame.bulletY = 480
            mainGame.bullet_state = "ready"
            mainGame.score_value += 1
            mainGame.enemyX[i] = random.randint(0, 736)
            mainGame.enemyY[i] = random.randint(50, 150)

        enemy(mainGame.enemyX[i], mainGame.enemyY[i], i)

    # Bullet Movement
    if mainGame.bulletY <= 0:
        mainGame.bulletY = 480
        mainGame.bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(mainGame.bulletX, mainGame.bulletY)
        mainGame.bulletY -= mainGame.bulletY_change

    player(mainGame.playerX, mainGame.playerY)
    show_score(mainGame.textX, mainGame.testY)
    pygame.display.update()


# Game Loop
running = True
while running:
    gameLoop()