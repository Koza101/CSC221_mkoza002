import pygame

class Rocket:
    """A class to manage the Rocket"""
    def __init__(self, ai_game):
        """Initialize the game charactrer and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.rsettings = ai_game.rsettings

    # Load the ship image and get its rect.
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()

    # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the rockets position based on the movement flags."""
        # Update the ships x value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rsettings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rsettings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rsettings.rocket_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.rsettings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)