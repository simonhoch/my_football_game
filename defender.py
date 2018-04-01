import pygame
from pygame.sprite  import Sprite

class Defender(Sprite):
    """A calss to represent a single alien in the fleet."""

    def __init__(self,  ai_settings, screen):
        """Initialize the defender  and set its starting position."""
        super(Defender, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the defender image and set its rect attribute.
        self.image = pygame.image.load('images/REAL.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new defender near the top right of the screen.
        self.rect.x = self.screen_rect.right - self.rect.width
        self.rect.y = self.screen_rect.top

        # Store the defender's exact position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the defender at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Move the defender down or up."""
        self.y += (self.ai_settings.defender_speed_factor *
                self.ai_settings.defense_direction)
        self.rect.y = self.y
