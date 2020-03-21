import math
import random
import pygame
from ui import UI
from pygame import mixer
from player import Player
from enemy import Enemy
from bullet import Bullet
from level import Level


class Game():
    def __init__(self):
        # Intialize the pygame
        pygame.init()
        self.ui = UI(800, 600)
        # Caption and Icon
        pygame.display.set_caption(self.ui.name)
        pygame.display.set_icon(self.ui.icon)
        self.china_enemy_types = ["img/cat.png",
                                  "img/chopsticks.png", "img/fan.png"]
        self.italy_enemy_types = ["img/italian_hand.png",
                                  "img/pizza.png", "img/wallet.png"]
        self.spanish_enemy_types = ["img/fork.png",
                                  "img/knife.png", "img/wallet.png"]
        self.isGameFinished = False
        

    def run(self):
        self.level1 = Level(self.ui, self.china_enemy_types, 7)
        if self.level1.run():
            self.ui.set_background('img/backgrounds/italy.png')
            self.level2 = Level(self.ui, self.italy_enemy_types, 12)
            if self.level2.run():
                self.ui.set_background('img/backgrounds/spain.jpg')
                self.level3 = Level(self.ui, self.spanish_enemy_types, 17, final_level=True)
                self.level3.run()
        Level.score_value = 0