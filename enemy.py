from pygame import transform, image

class Enemy:
    def __init__(self, img , x, y, x_change, y_change):
        self.width = 64
        self.height = 64
        self.enemyImg = transform.scale(image.load(img),(self.width, self.height))
        self.enemyX = x
        self.enemyY = y
        self.enemyX_change = x_change
        self.enemyY_change = y_change