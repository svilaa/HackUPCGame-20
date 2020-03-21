import pygame
import random
import math

class MainGame():
    def __init__(self):
        # Player
        self.playerImg = pygame.image.load('space_img/player.png')
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0

        # Enemy
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_of_enemies = 6

        self.china_enemy_types=["img/cat.png", "img/chopsticks.png", "img/fan.png"]
        for i in range(self.num_of_enemies):
            self.enemyImg.append(pygame.transform.scale(pygame.image.load(self.china_enemy_types[random.randint(0,2)]),(64,64)))
            self.enemyX.append(random.randint(0, 736))
            self.enemyY.append(random.randint(50, 150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)

        # Bullet

        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving

        self.bulletImg = pygame.image.load('space_img/bullet.png')
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = "ready"

        # Score

        self.score_value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.textX = 10
        self.testY = 10

        # Game Over
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)