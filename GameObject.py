import pygame
from until import Until

class GameObject:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.sprite = pygame.surface

        self.speed = 0

        self.x = 0
        self.y = 0

        self.dx = 0
        self.dy = 0

        self.group = list()

    def update(self):
        self.move()
        self.collision_with_walls

    def move(self):
        self.x += self.dx*self.speed
        self.y += self.dy*self.speed

    def collision_with_walls(self):
        if self.x > Until.WINDOW_SIZE:
            self.x = 0
        elif self.x < 0:
            self.x = Until.WINDOW_SIZE
        elif self.y < 0:
            self.y = Until.WINDOW_SIZE
        elif self.y > Until.WINDOW_SIZE:
            self.y = 0

    def on_collision_enter(self):
        pass

    def death(self):
        pass

    def render(self):
        pass

