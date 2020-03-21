import math
import random
import pygame
from ui import UI
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
import time

class Level:
    score_value = 0
    def __init__(self, ui, enemies_img, num_of_enemies, final_level=False):
        self.ui = ui
        self.running = True
        self.max_score = Level.score_value+100
        self.enemies_img = enemies_img
        self.final_level = final_level
        self.num_of_enemies = num_of_enemies
        self.init_level()
        

    def run(self):
        print("LEVEL UP")
        print(self.max_score)
        print(Level.score_value)
        # Game Loop
        while self.running and Level.score_value<self.max_score:
            self.gameLoop()
        if self.running==False:
            time.sleep(3)
        else:
            time.sleep(2)
        return self.running
        

    def init_level(self):
         # Player
        self.player = Player('img/glove.png',
                             self.ui.width/2, self.ui.height-10)

        # Enemy

        self.enemy_list = []
        print(self.__dict__)
        for i in range(self.num_of_enemies):
            self.enemy_list.append(Enemy(self.enemies_img[random.randint(
                0, 2)], random.randint(0, self.ui.width-64), random.randint(50, 150)*-1, 0.5, 0.4))

        # Bullet
        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        self.bullet = Bullet("img/bullets/soap3.png", 0,
                             self.player.playerY, 0, 7)

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
        over_text = self.over_font.render("GAME OVER", True, (0,0,0))
        self.ui.screen.blit(over_text, (200, 250))
    
    def level_up_text(self):
        over_text = self.over_font.render("LEVEL UP", True, (0,0,0))
        self.ui.screen.blit(over_text, (230, 250))

    def you_win(self):
        self.over_font = pygame.font.Font('freesansbold.ttf', 32)
        over_text = self.over_font.render("YOU'VE DESTROYED CORONAVIRUS!", True, (0,0,0))
        self.ui.screen.blit(over_text, (100, 250))

    def player_rend(self, x, y):
        self.ui.screen.blit(self.player.playerImg, (x, y))

    def enemy_rend(self, i):
        self.ui.screen.blit(
            self.enemy_list[i].enemyImg, (self.enemy_list[i].enemyX, self.enemy_list[i].enemyY))

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

        # Enemy Movement
        for i in range(self.num_of_enemies):

            # Game Over
            if self.enemy_list[i].enemyY + self.enemy_list[i].height > self.player.playerY:
                for j in range(self.num_of_enemies):
                    self.enemy_list[i].enemyY = self.ui.height + 500
                self.game_over_text()
                self.running = False
            elif Level.score_value>=self.max_score and not self.final_level:
                self.level_up_text()
            elif Level.score_value>=self.max_score and self.final_level:
                self.you_win()
            self.enemy_list[i].enemyY += self.enemy_list[i].enemyY_change

            self.enemy_list[i].enemyX += self.enemy_list[i].enemyX_change
            if self.enemy_list[i].enemyX <= 0:
                self.enemy_list[i].enemyX_change *= -1
            elif self.enemy_list[i].enemyX >= self.ui.width-self.enemy_list[i].width:
                self.enemy_list[i].enemyX_change *= -1

            # Collision
            collision = self.isCollision(
                self.enemy_list[i].enemyX, self.enemy_list[i].enemyY, self.bullet.bulletX, self.bullet.bulletY)
            if collision:
                explosionSound = mixer.Sound("space_img/explosion.wav")
                explosionSound.set_volume(0.1)
                explosionSound.play()
                self.bullet.bulletY = self.player.playerY + self.bullet.height
                self.bullet.bullet_state = "ready"
                Level.score_value += 5
                self.enemy_list[i].enemyX = random.randint(
                    0, self.ui.width - self.enemy_list[i].width)
                self.enemy_list[i].enemyY = random.randint(50, 150)*-1

            self.enemy_rend(i)

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