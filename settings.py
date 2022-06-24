import pygame

# Window variables setup
FPS = 60

# Basic colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Use the display resolution to size the window
pygame.init()
displayInfo = pygame.display.Info()
WIDTH = int(displayInfo.current_w * 2 / 3)
HEIGHT = int(displayInfo.current_h * 2 / 3)