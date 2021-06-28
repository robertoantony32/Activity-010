import pygame
from Entities.game_object import GameObject

class Player(GameObject):
    def __init__(self):
        super().__init__()
        
        self.life = 0

    def rotate(self):
        pass

    def shoot(self):
        pass

        

