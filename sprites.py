import pygame
from settings import *

class Square(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        pass