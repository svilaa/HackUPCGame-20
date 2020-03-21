from pygame import transform, image


class Player:
    def __init__(self, img, x, y):
        self.width = 64
        self.height = 64
        self.playerImg = transform.scale(image.load(img), (self.width, self.height))
        self.playerX = x - (self.width/2)
        self.playerY = y - (self.height)
        self.playerX_change = 0
