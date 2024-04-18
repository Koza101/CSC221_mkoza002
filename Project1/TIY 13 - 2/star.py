# TIY 13 - 1 Stars

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Creating a single star sprite"""
    
    def __init__(self, star_grid):
        """Create the star and set it's starting position on screen"""
        
        super().__init__()
        self.screen = star_grid.screen
        
        # Load the star image and set it's rect attribute
        
        self.image = pygame.image.load('star.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)