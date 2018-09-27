import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in a fleet"""

    def __init__(self, game_settings, screen):
        """init the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien in its current position"""
        self.screen.blit(self.image, self.rect)