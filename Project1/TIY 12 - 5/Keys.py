import sys

import pygame
from settings import Settings

class Keys:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        

        pygame.display.set_caption("Key Game")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            

    def _check_events(self):
        """Responding to keyboard inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responding to keyboard inputs"""
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update and flip the screen"""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    ai = Keys()
    ai.run_game()