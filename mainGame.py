import math
import random
import pygame
from pygame import mixer

class MainGame():
    def __init__(self):
        # Intialize the pygame
        pygame.init()

        # create the screen
        self.screen = pygame.display.set_mode((800, 600))

        # Background
        self.background = pygame.image.load('space_img/background.png')

        # Sound
        mixer.music.load("space_img/background.wav")
        mixer.music.play(-1)

        # Caption and Icon

        pygame.display.set_caption("Corona Invaiders")
        self.icon = pygame.image.load('img/virus.png')

        pygame.display.set_icon(self.icon)

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
        self.textY = 10

        # Game Over
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_score(self, x, y):
        score = self.font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (x, y))


    def game_over_text(self):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (200, 250))


    def player(self, x, y):
        self.screen.blit(self.playerImg, (x, y))


    def enemy(self, x, y, i):
        self.screen.blit(self.enemyImg[i], (x, y))


    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (x + 16, y + 10))


    def isCollision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False

    def gameLoop(self):
        # RGB = Red, Green, Blue
        self.screen.fill((0, 0, 0))
        # Background Image
        self.screen.blit(self.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if self.bullet_state is "ready":
                        bulletSound = mixer.Sound("space_img/laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        self.bulletX = self.playerX
                        self.fire_bullet(self.bulletX, self.bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        self.playerX += self.playerX_change
        if self.playerX <= 0:
            self.playerX = 0
        elif self.playerX >= 736:
            self.playerX = 736

        # Enemy Movement
        for i in range(self.num_of_enemies):

            # Game Over
            if self.enemyY[i] > 440:
                for j in range(self.num_of_enemies):
                    self.enemyY[j] = 2000
                self.game_over_text()
                break

            self.enemyX[i] += self.enemyX_change[i]
            if self.enemyX[i] <= 0:
                self.enemyX_change[i] = 4
                self.enemyY[i] += self.enemyY_change[i]
            elif self.enemyX[i] >= 736:
                self.enemyX_change[i] = -4
                self.enemyY[i] += self.enemyY_change[i]

            # Collision
            collision = self.isCollision(self.enemyX[i], self.enemyY[i], self.bulletX, self.bulletY)
            if collision:
                explosionSound = mixer.Sound("space_img/explosion.wav")
                explosionSound.play()
                self.bulletY = 480
                self.bullet_state = "ready"
                self.score_value += 1
                self.enemyX[i] = random.randint(0, 736)
                self.enemyY[i] = random.randint(50, 150)

            self.enemy(self.enemyX[i], self.enemyY[i], i)

        # Bullet Movement
        if self.bulletY <= 0:
            self.bulletY = 480
            self.bullet_state = "ready"

        if self.bullet_state is "fire":
            self.fire_bullet(self.bulletX, self.bulletY)
            self.bulletY -= self.bulletY_change

        self.player(self.playerX, self.playerY)
        self.show_score(self.textX, self.textY)
        pygame.display.update()

    def run(self):
        # Game Loop
        running = True
        while running:
            self.gameLoop()