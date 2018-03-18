import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    """A clas to manage ball kicked from the attacker."""

    def __init__(self, ai_settings, screen, attacker):
        """Create a ball abject at the attacker's current position."""
        super(Ball, self).__init__()
        self.screen = screen

        # Load the ball image and get its rect.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.bottom = attacker.rect.bottom
        self.rect.right = attacker.rect.right

        # Store ball's postion as a decimal value.
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.ball_speed_factor

    def update(self):
        """Move  the ball on the righ of the screen."""
        # Update the decimal position of the ball.
        self.x += self.speed_factor
        # Update the rect postion.
        self.rect.x = self.x

    def draw_ball(self):
        """Draw the ball to the screen."""
        self.screen.blit(self.image, self.rect)
