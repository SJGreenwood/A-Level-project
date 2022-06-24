import pygame
from settings import *

from pygame import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, position):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.game = game

        self.position = Vector2(position)
        self.velocity = Vector2()

    def update(self):
        """Update the player"""

        self.handleInput()

        self.velocity *= FRICTION
        self.position +=  self.velocity

        self.rect.center = self.position

    def handleInput(self):
        """Respond to keyboard input"""

        keys = pygame.key.get_pressed()

        movementVector = Vector2()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            movementVector.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            movementVector.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            movementVector.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            movementVector.x += 1

        if movementVector:
            self.velocity += movementVector.normalize() * CHARACTER_SPEED * self.game.deltaT