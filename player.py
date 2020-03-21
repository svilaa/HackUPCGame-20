from pygame import transform,image

class Player:
    def __init__(self, x, y):
        self.width = 64
        self.height = 64
        self.playerImg = transform.scale(image.load('space_img/player.png'),(64,64))
        self.playerX = x - (self.width/2)
        self.playerY = y - (self.height)
        self.playerX_change = 0