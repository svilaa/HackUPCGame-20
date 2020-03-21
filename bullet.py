from pygame import image, transform

class Bullet:
    def __init__(self, img, x, y, x_change, y_change):
        self.height=32
        self.width=32
        self.bulletImg = transform.scale(image.load(img),(self.height,self.width))
        self.bulletX = x
        self.bulletY = y
        self.bulletX_change = x_change
        self.bulletY_change = y_change
        self.bullet_state = "ready"