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
        self.china_music = "music/chinese_level.mp3"
        self.italia_music = "music/italian_level.mp3"
        self.spain_music = "music/spanish_level.mp3"
        self.final_boss_music = "music/final_bos.mp3"

        self.isGameFinished = False
        

    def run(self):
        self.level1 = Level(self.ui, self.china_enemy_types, 7, self.china_music)
        self.ui.set_sound(self.china_music)
        if self.level1.run():
            self.ui.set_sound(self.italia_music)
            self.ui.set_background('img/backgrounds/italy.png')
            self.level2 = Level(self.ui, self.italy_enemy_types, 12, self.italia_music)
            if self.level2.run():
                self.ui.set_sound(self.spain_music)
                self.ui.set_background('img/backgrounds/spain.jpg')
                self.level3 = Level(self.ui, self.spanish_enemy_types, 17, self.spain_music, final_level=True)
                self.level3.run()
        self.isGameFinished = True
