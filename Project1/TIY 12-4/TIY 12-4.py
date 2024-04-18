import sys

import pygame

from rsettings import Rsettings
from rocket import Rocket

class Rocket:

    def __init__(self):
        pygame.init()
        self.rsettings = Rsettings()

        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("TIY 12 - 4")
        self.bg_color = (255, 255, 255)

        self.rocket = Rocket(self)



    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.screen.fill(self.bg_color)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

            
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.rsettings.bg_color)
        self.rocket.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = Rocket()
    ai.run_game()