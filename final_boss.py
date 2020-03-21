import math
import random
import pygame
from ui import UI
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from level import Level
import time


class FinalBoss:
    def __init__(self, ui):
        self.ui = ui
        self.running = True
        self.max_score = Level.score_value + 70
        self.init_level()

    def run(self):
        # Game Loop
        while self.running:
            self.gameLoop()
        if self.running == False:
            time.sleep(3)

    def init_level(self):
        # Player
        self.player = Player('img/glove.png',
                             self.ui.width/2, self.ui.height-10)
        # Bullet
        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        self.bullet = Bullet("img/bullets/soap3.png", 0,
                             self.player.playerY, 0, 12)

        self.boss = Enemy("img/coronavirus.png", random.randint(0, self.ui.width-90),
                     random.randint(50, 150)*-1, 2.5, 0.4, 90, 90)
        # Score
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.textX = 10
        self.textY = 10
        # Game Over
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(self, x, y):
        score = self.font.render(
            "Score : " + str(Level.score_value), True, (255, 255, 255))
        self.ui.screen.blit(score, (x, y))

    def game_over_text(self):
        over_text = self.over_font.render("GAME OVER", True, (0, 0, 0))
        self.ui.screen.blit(over_text, (200, 250))

    def you_win(self):
        self.over_font = pygame.font.Font('freesansbold.ttf', 32)
        over_text = self.over_font.render(
            "YOU'VE DESTROYED CORONAVIRUS!", True, (255, 255, 255))
        self.ui.screen.blit(over_text, (100, 250))

    def player_rend(self, x, y):
        self.ui.screen.blit(self.player.playerImg, (x, y))

    def boss_rend(self):
        self.ui.screen.blit(self.boss.enemyImg,
                            (self.boss.enemyX, self.boss.enemyY))

    def fire_bullet(self, x, y):
        self.bullet.bullet_state = "fire"
        self.ui.screen.blit(self.bullet.bulletImg, (x + 16, y + 10))

    def isCollision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) +
                             (math.pow(enemyY - bulletY, 2)))
        return distance < 27

    def gameLoop(self):
        # RGB = Red, Green, Blue
        self.ui.screen.fill((0, 0, 0))
        # Background Image
        self.ui.screen.blit(self.ui.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    self.player.playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if self.bullet.bullet_state is "ready":
                        bulletSound = mixer.Sound("space_img/laser.wav")
                        bulletSound.set_volume(0.1)
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        self.bullet.bulletX = self.player.playerX
                        self.fire_bullet(self.bullet.bulletX,
                                         self.bullet.bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.playerX_change = 0

        self.player.playerX += self.player.playerX_change
        if self.player.playerX <= 0:
            self.player.playerX = 0
        elif self.player.playerX >= self.ui.width-self.player.width:
            self.player.playerX = self.ui.width-self.player.width

        # Game Over
        if self.boss.enemyY + self.boss.height > self.player.playerY:
            self.boss.enemyY = self.ui.height + 500
            self.game_over_text()
            self.running = False
        elif Level.score_value >= self.max_score:
            self.you_win()
            self.running = False

        self.boss.enemyY += self.boss.enemyY_change
        self.boss.enemyX += self.boss.enemyX_change
        if self.boss.enemyX <= 0:
            self.boss.enemyX_change *= -1
        elif self.boss.enemyX >= self.ui.width-self.boss.width:
            self.boss.enemyX_change *= -1

        # Collision
        collision = self.isCollision(
            self.boss.enemyX, self.boss.enemyY, self.bullet.bulletX, self.bullet.bulletY)
        if collision:
            explosionSound = mixer.Sound("space_img/explosion.wav")
            explosionSound.set_volume(0.1)
            explosionSound.play()
            self.bullet.bulletY = self.player.playerY + self.bullet.height
            self.bullet.bullet_state = "ready"
            Level.score_value += 10
        self.boss_rend()
        # Bullet Movement
        if self.bullet.bulletY <= 0:
            self.bullet.bulletY = self.player.playerY + self.bullet.height
            self.bullet.bullet_state = "ready"

        if self.bullet.bullet_state is "fire":
            self.fire_bullet(self.bullet.bulletX, self.bullet.bulletY)
            self.bullet.bulletY -= self.bullet.bulletY_change

        self.player_rend(self.player.playerX, self.player.playerY)
        self.show_score(self.textX, self.textY)
        pygame.display.update()
