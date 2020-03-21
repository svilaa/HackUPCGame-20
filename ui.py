from pygame import display, image, mixer, transform


class UI:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # create the screen
        self.screen = display.set_mode((self.width, self.height))
        # Background
        self.background = transform.scale(image.load(
            'img/backgrounds/china2.jpg'), (self.width, self.height))
        # Sound
        self.sound = mixer.music
        self.sound.load("space_img/background.wav")
        self.sound.set_volume(0.1)
        self.sound.play(-1)
        # Icon
        self.icon = image.load('img/virus.png')
        # Name
        self.name = "Corona Invaders"
