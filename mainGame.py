class MainGame():
    def __init__(self):
        # Player
        self.playerImg = pygame.image.load('space_img/player.png')
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0