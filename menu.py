import pygame

class Menu:
    def __init__(self):
        self.intro = True
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = ((0,255,0))
        self.block_color = (53,115,255)
        self.car_width = 73
        self.clock = pygame.time.Clock()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def run(self):
         while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                print(pygame.event)
                if event.type == pygame.K_SPACE:
                    self.intro=False
                    print(pygame.event)
            self.gameDisplay.fill(self.white)
            largeText = pygame.font.Font('freesansbold.ttf',115)
            TextSurf, TextRect = self.text_objects("A bit Racey", largeText)
            TextRect.center = ((self.display_width/2),(self.display_height/2))
            self.gameDisplay.blit(TextSurf, TextRect)

            pygame.draw.rect(self.gameDisplay, self.green,(150,450,100,50))
            pygame.draw.rect(self.gameDisplay, self.red,(550,450,100,50))


            pygame.display.update()
            self.clock.tick(15)