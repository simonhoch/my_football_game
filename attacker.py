import pygame

class Attacker():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the attacker image and get its rect.
        self.image = pygame.image.load('images/PSG.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new attacker at the center of the screen.
        self.rect.centerx = 0 + self.rect.width
        self.rect.centery = self.screen_rect.centery

        #Store a decimal value for the attacker's center.
        self.centerx = float(self.rect.x)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the attacker's position based on the movement flag."""
        # Update the attacker's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.attacker_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.attacker_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.attacker_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.attacker_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def replace_attacker(self):
        """Replace attacker on the initial position."""
        self.centerx = 0 + (self.rect.width / 2)
        self.centery = self.screen_rect.centery
