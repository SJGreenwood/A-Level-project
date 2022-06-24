import pygame

from settings import *

class Game:
    def __init__(self):
        """Initialise game window, mixer and clock"""

        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Stealth game")
        self.clock = pygame.time.Clock()

    def new(self):
        """Setup new game"""
        pass

    def run(self):
        """The game's game loop"""

        self.running = True
        while self.running:
            # Keep loop running at the right speed and get the time since the last frame
            self.deltaT = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Process input"""

        for event in pygame.event.get():
            # Check for closing window
            if event.type == pygame.QUIT:
                quit()

    def update(self):
        """Update all the sprites"""
        pass

    def draw(self):
        """Draw all the sprites and flip the display"""
        self.screen.fill(BLACK)

        pygame.display.flip()


game = Game()

while True:
    game.new()
    game.run()