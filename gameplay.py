import pygame
from pygame.locals import *
from until import Until


class Gameplay:
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((Until.WINDOWM_SIZE, Until.WINDOW_SIZE))
        self.clock  = pygame.time.Clock()

        self.running = True


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False


            self.screen.fill(Until.BLACK)

            self.update()
            self.render()
            
            pygame.display.flip()
            self.clock.tick(60)

    def update(self):
        pass

    def render(self):
        pass